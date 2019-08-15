from PyQt5.Qt import *
from WK import WKColor
from urwid.util import str_util # Use this to determine the actual width of strings with japanese chars present

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
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setMinimumSize(QSize(0, 0))
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(3)
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("promptLabel")

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
        text_len = self.getTextLength()
        w = self.width() / (text_len) * 1.5
        h = self.height() * 0.6
        font.setPixelSize( w if w < h else h )
        # print("WIDTH {} x HEIGHT {}".format(w, h))

        self.setFont(font)

    def getTextLength( self ):
        l = 0
        for char in self.text():
            l += str_util.get_width( ord( char ) )

        return( l )
