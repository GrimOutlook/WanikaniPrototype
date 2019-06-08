from WanikaniSession import WanikaniSession
from WanikaniDatabase import WanikaniDatabase
from UI_Widget import UI_Widget

if __name__ == "__main__":
    wk = WanikaniSession()
    wk.getAPIResults()
    wk.printAPIResults()

    # app = QApplication( [] )

    # Widget = QWidget()
    # ui = UI_Widget()
    # ui.setupUI( Widget )

    # Widget.show()
    # sys.exit( app.exec_() )


