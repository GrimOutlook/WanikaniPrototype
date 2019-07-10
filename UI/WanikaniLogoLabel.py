from PyQt5.Qt import *

class WanikaniLogoLabel( QLabel ):
    def __init__( self, parent ):
        super().__init__( parent = parent )

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 55))
        self.setBaseSize(QSize(0, 0))
