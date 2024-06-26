import sys
sys.path.append("../")
sys.path.append("../WK")

from PyQt5.Qt import *

from WK import Pages
from settings import Settings
from ReviewWidget import ReviewWidget
from HomeWidget import HomeWidget

class MainWindow( QMainWindow ):
    def __init__( self, *args ):
        self.settings = Settings( Pages.MAIN_WINDOW )
        QMainWindow.__init__(self, *args)

        self.setWindowTitle("WanikaniPrototype")

        startup_height = self.settings.settings["main_window"]["startup_height"]
        startup_width = self.settings.settings["main_window"]["startup_width"]
        self.resize( startup_height, startup_width )

        self.setObjectName("MainWindow")
        self.openPage( self.settings.settings["main_window"]["startup_page"] )

    def openPage( self, page ):
        if( page == Pages.HOME_PAGE ):
            self.cw = HomeWidget( self )
        elif( page == Pages.REVIEW_PAGE ):
            self.cw = ReviewWidget( self )
        else:
            raise Exception("Unknown page specification. Page specified is {}".format(page))

        self.setCentralWidget( self.cw )
        self.cw.show()

    def resizeEvent( self, evt ):
        # print( self.size() )
        self.settings.settings["main_window"]["startup_height"] = self.size().height()
        self.settings.settings["main_window"]["startup_width"] = self.size().width()

    def keyPressEvent( self, e ):
        if( e.key() == Qt.Key_Q  and e.modifiers() & Qt.ControlModifier ):
            self.close()

    def syncReviews( self ):
        pass

    def closeEvent( self, e ):
        self.syncReviews()
        self.settings.saveSettings()
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
