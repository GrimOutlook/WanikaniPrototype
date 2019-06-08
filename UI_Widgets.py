from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class UI_Widget():
    def setupUI( self, Widget ):
        # Widget.setGeometry( 1000, 1000, 500, 500 )
        Widget.setWindowTitle("WanikaniPrototype")
        Widget.resize( 500, 500 )

        self.layout = QVBoxLayout()

        self.prompt_label = QLabel("Prompt...")
        self.layout.addWidget( self.prompt_label )

        self.send_button = QPushButton()
        self.layout.addWidget( send_button )

        Widget.setLayout( self.layout )

