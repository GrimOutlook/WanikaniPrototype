from PyQt5.Qt import *

"""
##### TODO #####
Change font to something better. Better yet allow choice of font
"""

class PromptTypeLabel( QLabel ):
    def __init__( self, parent ):
        super().__init__( parent = parent )

        self.stylesheets = {
            "meaning" : "background-color : white; color : black",
            "reading" : "background-color : black; color : white"
        }

    def setPromptStyle( self, prompt_type ):
        self.setStyleSheet( self.stylesheets[ prompt_type ] )

    def resizeEvent( self, e ):
        super().resizeEvent( e )

        QFrame.resizeEvent( self, e )
        font = self.font()
        font.setPixelSize(self.height() * 0.60)

        self.setFont(font)
