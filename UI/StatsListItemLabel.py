from PyQt5.Qt import *
from WK import WK

class StatsListItemLabel( QLabel ):
    def __init__( self, parent, typ, item ):
        super().__init__( parent = parent )
        self.parent = parent
        self.typ = typ
        self.item = item
        self.setMinimumSize( 200, 30 )
        self.setSizePolicy( QSizePolicy.Preferred, QSizePolicy.Preferred )

    def getColorScheme( self ):
        if( self.item == WK.TOP_LABEL or self.item == WK.BOTTOM_LABEL ):
            fill_color =  WK.ACCENT_GRAY
        elif( self.item["subject_type"] == "radical" ):
            fill_color = WK.RADICAL_BLUE
        elif( self.item["subject_type"] == "kanji" ):
            fill_color = WK.KANJI_PINK
        elif( self.item["subject_type"] == "vocabulary" ):
            fill_color = WK.VOCABULARY_PURPLE
        else:
            raise Exception("Unknown item type. Item type is {}".format( self.item ))

        return( fill_color )

    def getText( self ):
        if( self.item == WK.TOP_LABEL):
            return("NEW UNLOCKS IN THE LAST 30 DAYS")

        elif(self.item == WK.BOTTOM_LABEL ):
            return( "SEE MORE UNLOCKS..." )

        else:
            if( self.typ == WK.NEW_UNLOCKS ):
                subject_info = self.parent.wk_db.getObjectBySubjectID( self.item["subject_id"], self.item["subject_type"] )
                return( subject_info["characters"], self.item["unlocked_datetime"] )

    def paintEvent( self, evt ):
        fill_color = self.getColorScheme()
        text = self.getText()

        print("Fill color is {}".format( fill_color ))
        print("Text is {}".format( text ))

        pixmap = QPixmap(self.width(), self.height())
        pixmap.fill( QColor(fill_color ) )

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setFont( QFont("Arial", self.size().height()/3 ) );
        if( self.item == WK.TOP_LABEL or self.item == WK.BOTTOM_LABEL ):
            painter.setPen( QPen( QColor( 24, 26, 27, 0.8 ), 1, Qt.SolidLine) )
            painter.drawText( QRect( 0, 0+1, self.width(), self.height() ), Qt.AlignCenter, text );

            painter.setPen( QPen( Qt.white, 1, Qt.SolidLine) )
            painter.drawText( QRect( 0, 0, self.width(), self.height() ), Qt.AlignCenter, text );

        else:
            painter.setPen( QPen( QColor( 24, 26, 27, 0.8 ), 1, Qt.SolidLine) )
            painter.drawText( QRect( 0, 0+1, self.width(), self.height() ), Qt.AlignLeft, text[0] );

            painter.setPen( QPen( Qt.white, 1, Qt.SolidLine) )
            painter.drawText( QRect( 0, 0, self.width(), self.height() ), Qt.AlignLeft, text[0] );

            painter.setPen( QPen( QColor( 24, 26, 27, 0.8 ), 1, Qt.SolidLine) )
            painter.drawText( QRect( 0, 0+1, self.width(), self.height() ), Qt.AlignRight, text[1] );

            painter.setPen( QPen( Qt.white, 1, Qt.SolidLine) )
            painter.drawText( QRect( 0, 0, self.width(), self.height() ), Qt.AlignRight, text[1] );

        self.setPixmap( pixmap )
        return( super().paintEvent( evt ) )
