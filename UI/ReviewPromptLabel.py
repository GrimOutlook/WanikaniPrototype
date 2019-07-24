from PyQt5.Qt import *
from WK import WKColor

"""
##### TODO ####
1) Implement changing fonts and implement changing font on every new review item
2) Fix resizing, its okay right now, but might be made better with more effort
3) Implement custom context menu (right-click) so that you can copy the kanji from the prompt
4) Convert text label into pixmap label so color changin is easier
"""

class ReviewPromptLabel( QLabel ):
    def __init__( self, parent ):
        super().__init__(parent=parent)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.stylesheets = {
            "vocabulary" : "background-color : {}".format( WKColor.VOCABULARY_PURPLE ),
            "kanji" : "background-color : {}".format( WKColor.KANJI_PINK ),
            "radical" : "background-color : {}".format( WKColor.RADICAL_BLUE )
        }

    def setStyle( self, subject_type ):
        self.setStyleSheet( self.stylesheets[ subject_type ] )

    def resizeEvent( self, e ):
        super(ReviewPromptLabel, self).resizeEvent( e )
        # print( "resizeEvent", e.size().width(), e.size().height() )
        QFrame.resizeEvent( self, e )
        font = self.font()
        if( self.width() * 0.40 < self.height() * 0.75 ):
            font.setPixelSize(self.width() * 0.40)
        else:
            font.setPixelSize(self.height() * 0.75)

        br = QFontMetrics( font ).boundingRect( self.text() )
        cr = self.contentsRect()
        # print( "BR: " + str(br.width()) + " x " + str( br.height()  ))
        # print( "CR: " + str(cr.width()) + " x " + str(cr.height()) + "\n" )

        self.setFont(font)
