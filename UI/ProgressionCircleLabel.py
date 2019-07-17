from PyQt5.Qt import *
from WK import WKColor

"""
##### TODO #####
1) Implement custom right click menu to allow copying of kanji
"""

class ProgressionCircleLabel( QLabel ):
    def __init__( self, parent, obj ):
        super().__init__( parent = parent )
        self.parent = parent
        self.obj = obj
        self.text = self.obj.characters
        self.subject_type = self.obj.object

        self.srs_stage = self.obj.assignment.srs_stage
        self.available_datetime = self.obj.assignment.available_datetime
        print( self.obj.wk_db )

        # self.size_hint = self.parent.size().width()/25
        self.setMinimumSize( 30, 30 )
        # self.setMaximumSize( self.parent.clpi_size_hint+2, self.parent.clpi_size_hint+2 )
        self.setContentsMargins( 0,0,0,0 )
        # self.setStyleSheet("""
                           # padding: 0px;
                           # margin: 0px;
                           # border-width: 0px;
                           # border-color: black;
                           # """)
        self.setSizePolicy( QSizePolicy.Preferred, QSizePolicy.Preferred )

    def paintEvent(self, event):

        if( self.subject_type == "radical" ):
            primary_color = WKColor.RADICAL_BLUE
            mask_color = WKColor.RADICAL_PROGRESSION_MASK_BLUE
            done_color = WKColor.RADICAL_PROGRESSION_DONE_BLUE
        elif( self.subject_type == "kanji" ):
            primary_color = WKColor.KANJI_PINK
            mask_color = WKColor.KANJI_PROGRESSION_MASK_PINK
            done_color = WKColor.KANJI_PROGRESSION_DONE_PINK

        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill( Qt.transparent )

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        circle_x = self.width() * 0.05
        circle_y = self.height() * 0.05

        circle_width = self.width() * 0.9
        circle_height = self.height() * 0.9

        if( self.obj.assignment.srs_stage < 5 ):
            painter.setBrush( QBrush( QColor( primary_color ), Qt.SolidPattern) )
            painter.setPen( QPen( QColor( primary_color ), 0, Qt.SolidLine) )
            painter.drawEllipse( circle_x, circle_y, circle_width, circle_height )

            if( self.available_datetime == None ):
                painter.setBrush( QBrush( QColor( mask_color ), Qt.BDiagPattern) )
                painter.drawEllipse( circle_x, circle_y, circle_width, circle_height )

            else:
                # This is where I will later make the semicircles that go around shoing the progress to guru for the object
                # Angles must be multiplied by 16 since every unit is 1/16 of a degree
                if( self.srs_stage == 2 ):
                    spanAngle = -90 * 16
                elif( self.srs_stage == 3 ):
                    spanAngle = -180 * 16
                elif( self.srs_stage == 4 ):
                    spanAngle = -270 * 16
                else:
                    spanAngle = 0

                startAngle = 90 * 16
                rc_x = 0
                arc_y = 0
                painter.setPen( QPen( QColor( mask_color ), circle_width/10, Qt.SolidLine) )
                painter.drawArc( circle_x, circle_y, circle_width, circle_height, startAngle, spanAngle )
        else:
            painter.setBrush( QBrush( QColor( done_color ), Qt.SolidPattern) )
            painter.setPen( QPen( QColor( done_color ), circle_width/10, Qt.SolidLine) )

            painter.drawEllipse( circle_x, circle_y, circle_width, circle_height )


        painter.setFont( QFont("Arial", self.size().width()/3 ) );
        painter.setPen( QPen( QColor( 24, 26, 27, 0.8 ), 1, Qt.SolidLine) )
        painter.drawText( QRect( 0, 0+1, self.width(), self.height() ), Qt.AlignCenter, self.text );

        painter.setPen( QPen( Qt.white, 1, Qt.SolidLine) )
        painter.drawText( QRect( 0, 0, self.width(), self.height() ), Qt.AlignCenter, self.text );

        self.setPixmap( pixmap )

        return( super().paintEvent( event ) )

    def resizeEvent( self, event ):
        event.accept()

        event_height = event.size().height()
        event_width = event.size().width()
        self.size_hint = self.parent.size().width()/self.parent.clk_layout_cutoff
        if( event_width > event_height ):
            self.resize( event_height, event_height )
        else:
            self.resize( event_width, event_width )


    def event( self, event ):
        if( event.type() == QEvent.Enter ):
            print("Hovering over " + self.text + "...")

        elif( event.type() == QEvent.Leave ):
            print("No longer hovering over " + self.text + "...")

        return( super().event( event ) )

    def mousePressEvent( self, evt ):
        print("clicked Label")
        super().mousePressEvent( evt )

    def heightForWidth( self, width ):
        return( width )

    def sizeHint( self ):
        self.parent.clpi_size_hint = self.parent.size().width()/25 - 10
        return( QSize( self.parent.clpi_size_hint, self.parent.clpi_size_hint ) )
