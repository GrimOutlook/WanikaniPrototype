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
            "vocabulary"    : "background-color : {}".format( WKColor.VOCABULARY_PURPLE ),
            "kanji"         : "background-color : {}".format( WKColor.KANJI_PINK ),
            "radical"       : "background-color : {}".format( WKColor.RADICAL_BLUE )
        }

    def setStyle( self, subject_type ):
        self.setStyleSheet( self.stylesheets[ subject_type ] )

    def resizeEvent( self, e ):
        """
        Do not ask me how this works, I have no idea why this works
        """
        super(ReviewPromptLabel, self).resizeEvent( e )
        # print( "resizeEvent", e.size().width(), e.size().height() )
        QFrame.resizeEvent( self, e )
        font = self.font()
        # I have no idea why these constants work, i got them from trial and error and will simply leave them here with no explanation
        w = self.width()/2 * 0.40
        h = self.height() * 0.5
        font.setPixelSize( w if w < h else h )
        # print("WIDTH {} x HEIGHT {}".format(w, h))

        self.setFont(font)
