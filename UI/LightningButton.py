from PyQt5.Qt import *

class LightningButton( QPushButton ):
    def __init__( self, lightning ):
        super().__init__()
        self.lightning = lightning
        self.setLightning( lightning )

    def setLightning( self, lightning ):
        mode = "on" if lightning == True else "off"
        self.setText( "Lightning: {}".format( mode ) )
