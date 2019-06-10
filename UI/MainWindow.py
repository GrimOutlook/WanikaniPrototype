import sys
from PyQt5.Qt import *

from ReviewWidget import ReviewWidget
from HomeWidget import HomeWidget

class MainWindow( QMainWindow ):
    def __init__( self, *args ):
        QMainWindow.__init__(self, *args)

        self.setWindowTitle("WanikaniPrototype")
        self.resize( 2000, 1000 )
        self.setObjectName("MainWindow")
        self.openReviews()
        self.openHomepage()

    def openReviews( self ):
        self.cw = ReviewWidget( self )
        self.setCentralWidget( self.cw )
        self.cw.show()

    def openHomepage( self ):
        self.cw = HomeWidget( self )
        self.setCentralWidget( self.cw )
        self.cw.show()


    def resizeEvent( self, evt ):
        # print( self.size() )
        pass

    def keyPressEvent( self, e ):
        if( e.key() == Qt.Key_Q  and e.modifiers() & Qt.ControlModifier ):
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
