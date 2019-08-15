from PyQt5.Qt import *

class LightningButton( QToolButton ):
    def __init__( self, lightning ):
        super().__init__()
        self.setPopupMode( QToolButton.DelayedPopup )

        # self.menu = QMenu()
        # self.initMenu( self.menu )
        # self.setMenu( self.menu )

        self.lightning = lightning
        self.setLightning( lightning )

    def setLightning( self, lightning ):
        mode = "🗲" if lightning == True else "⚡"
        self.setText( "{}".format( mode ) )

    # def initMenu( self, menu ):

        # menu.addAction()
