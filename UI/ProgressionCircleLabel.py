from PyQt5.Qt import *
from WKColor import WKColor

class ProgressionCircleLabel( QLabel ):
    def __init__( self, parent, obj, assignment_info ):
        super().__init__( parent = parent )
        size = 60
        self.setMinimumSize( 50, 50 )
        self.setMaximumSize( 150, 150 )
        self.setSizePolicy( QSizePolicy.Preferred, QSizePolicy.Preferred )

        self.obj = obj
        self.assignment_info = assignment_info
        self.text = self.obj["characters"]
        self.subject_type = self.obj["object"]

        #self.paintEvent()

    def paintEvent(self, event):

        if( self.subject_type == "radical" ):
            primary_color = WKColor.RADICAL_BLUE
        elif( self.subject_type == "kanji" ):
            primary_color = WKColor.KANJI_PINK
            mask_color = WKColor.KANJI_PROGRESSION_MASK_PINK

        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill( Qt.transparent )

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        circle_x = self.width() * 0.05
        circle_y = self.height() * 0.05

        circle_width = self.width() * 0.9
        circle_height = self.height() * 0.9

        if( self.assignment_info["srs_stage"] < 5 ):
            painter.setBrush( QBrush( QColor( primary_color ), Qt.SolidPattern) )
            painter.setPen( QPen( QColor( primary_color ), 0, Qt.SolidLine) )
            painter.drawEllipse( circle_x, circle_y, circle_width, circle_height )

            if( self.assignment_info["available_datetime"] == None ):
                painter.setBrush( QBrush( QColor( mask_color ), Qt.BDiagPattern) )
                painter.drawEllipse( circle_x, circle_y, circle_width, circle_height )

            else:
                # This is where I will later make the semicircles that go around shoing the progress to guru for the object
                # Angles must be multiplied by 16 since every unit is 1/16 of a degree
                if( self.assignment_info["srs_stage"] == 2 ):
                    spanAngle = -90 * 16
                elif( self.assignment_info["srs_stage"] == 3 ):
                    spanAngle = -180 * 16
                elif( self.assignment_info["srs_stage"] == 4 ):
                    spanAngle = -270 * 16
                else:
                    spanAngle = 0

                startAngle = 90 * 16
                arc_x = 0
                arc_y = 0
                painter.setPen( QPen( QColor( mask_color ), 10, Qt.SolidLine) )
                painter.drawArc( circle_x, circle_y, circle_width, circle_height, startAngle, spanAngle )
        else:
            primary_color = WKColor.KANJI_PROGRESSION_DONE_PINK
            painter.setBrush( QBrush( QColor( primary_color ), Qt.SolidPattern) )
            painter.setPen( QPen( QColor( primary_color ), 0, Qt.SolidLine) )
            painter.drawEllipse( circle_x, circle_y, circle_width, circle_height )


        painter.setFont( QFont("Arial", self.size().width()/3 ) );
        painter.setPen( QPen( QColor( 24, 26, 27, 0.8 ), 1, Qt.SolidLine) )
        painter.drawText( QRect( 0, 0+1, self.width(), self.height() ), Qt.AlignCenter, self.text );

        painter.setPen( QPen( Qt.white, 1, Qt.SolidLine) )
        painter.drawText( QRect( 0, 0, self.width(), self.height() ), Qt.AlignCenter, self.text );

        self.setPixmap( pixmap )

        return( super().paintEvent( event ) )

    def resizeEvent( self, event ):
        self.resize( event.size().width(), event.size().width() )


    def event( self, event ):
        if( event.type() == QEvent.Enter ):
            print("Hovering over " + self.text + "...")

        elif( event.type() == QEvent.Leave ):
            print("No longer hovering over " + self.text + "...")

        return( super().event( event ) )

    def mousePressEvent( self, evt ):
        print("clicked Label")
        super().mousePressEvent( evt )

    def sizeHint( self ):
        width = self.width()
        return( QSize( width, self.heightForWidth( width ) ) )

    def heightForWidth( self, width ):
        return( width )

    def sizeHint( self ):
        return( QSize( 50, 50 ) )
