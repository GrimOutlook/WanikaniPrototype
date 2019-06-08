from PyQt5 import QtCore as QC
from PyQt5 import QtGui as QG
from PyQt5 import QtWidgets as QW

from WanikaniSession import WanikaniSession
from WanikaniDatabase import WanikaniDatabase

import sys

class UI_MainWindow():
    def __init__( self ):
        self.app = QW.QApplication( [] )
        self.MainWindow = QW.QMainWindow()

        # MainWindow.setGeometry( 1000, 1000, 500, 500 )
        self.MainWindow.setWindowTitle("WanikaniPrototype")
        self.MainWindow.resize( 500, 500 )

        self.setupReviewScreen()

    def setupHomeScreen( self ):
        self.HomeScreen = QW.QWidget()
        self.MainWindow.setCentralWidget( self.ReviewScreen )

    def setupReviewScreen( self ):
        self.ReviewScreen = QW.QWidget()
        self.MainWindow.setCentralWidget( self.ReviewScreen )

        layout = QW.QVBoxLayout()

        prompt_label = QW.QLabel("Prompt...")
        prompt_label.setAlignment( QC.Qt.AlignCenter )
        layout.addWidget( prompt_label )

        prompt_type_label = QW.QLabel("Prompt type...")
        prompt_type_label.setAlignment( QC.Qt.AlignCenter )
        layout.addWidget( prompt_type_label )

        answer_box = QW.QLineEdit()
        answer_box.setAlignment( QC.Qt.AlignCenter )
        answer_box.setPlaceholderText("Answer")
        layout.addWidget( answer_box )

        send_button = QW.QPushButton( "Show Answer" )
        # send_button.setStyleSheet()
        layout.addWidget( send_button )

        self.ReviewScreen.setLayout( layout )

    def start( self ):
        self.MainWindow.show()
        sys.exit( self.app.exec_() )
