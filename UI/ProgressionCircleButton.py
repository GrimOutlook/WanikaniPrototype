from PyQt5.Qt import *

class ProgressionCircleButton( QPushButton ):
    def __init__( self, parent ):
        super().__init__( parent = parent )

        self.setMaximumSize(50,50)
        self.setSizePolicy( QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setStyleSheet("background-color : black; color : white")

    def resizeEvent(self, event):
        self.setMask(QRegion(self.rect(), QRegion.Ellipse))
        super().resizeEvent(event)
