# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReviewPageTypingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append("../WK/")
sys.path.append(".")

from PyQt5.Qt import *
from ReviewSession import ReviewSession

class ReviewWidget( QWidget ):
    def __init__(self, MainWindow):
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi( self )

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1616, 837)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.percentCorrect = QLabel(Form)
        self.percentCorrect.setObjectName("percentCorrect")
        self.horizontalLayout_2.addWidget(self.percentCorrect)
        self.totalDone = QLabel(Form)
        self.totalDone.setObjectName("totalDone")
        self.horizontalLayout_2.addWidget(self.totalDone)
        self.totalToDo = QLabel(Form)
        self.totalToDo.setObjectName("totalToDo")
        self.horizontalLayout_2.addWidget(self.totalToDo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.promptLabel = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setMinimumSize(QSize(300, 0))
        self.promptLabel.setFrameShape(QFrame.Box)
        self.promptLabel.setLineWidth(3)
        self.promptLabel.setAlignment(Qt.AlignCenter)
        self.promptLabel.setObjectName("promptLabel")
        self.horizontalLayout.addWidget(self.promptLabel)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radicalCountToDo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radicalCountToDo.sizePolicy().hasHeightForWidth())
        self.radicalCountToDo.setSizePolicy(sizePolicy)
        self.radicalCountToDo.setMinimumSize(QSize(40, 0))
        self.radicalCountToDo.setObjectName("radicalCountToDo")
        self.verticalLayout_3.addWidget(self.radicalCountToDo)
        self.kanjiCountToDo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kanjiCountToDo.sizePolicy().hasHeightForWidth())
        self.kanjiCountToDo.setSizePolicy(sizePolicy)
        self.kanjiCountToDo.setMinimumSize(QSize(40, 0))
        self.kanjiCountToDo.setObjectName("kanjiCountToDo")
        self.verticalLayout_3.addWidget(self.kanjiCountToDo)
        self.vocabularyCountToDo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vocabularyCountToDo.sizePolicy().hasHeightForWidth())
        self.vocabularyCountToDo.setSizePolicy(sizePolicy)
        self.vocabularyCountToDo.setMinimumSize(QSize(40, 0))
        self.vocabularyCountToDo.setObjectName("vocabularyCountToDo")
        self.verticalLayout_3.addWidget(self.vocabularyCountToDo)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.promptType = QLabel(Form)
        self.promptType.setMinimumSize(QSize(0, 75))
        self.promptType.setAlignment(Qt.AlignCenter)
        self.promptType.setObjectName("promptType")
        self.verticalLayout_2.addWidget(self.promptType)
        self.answerBox = QLineEdit(Form)
        self.answerBox.setMinimumSize(QSize(0, 75))
        self.answerBox.setAlignment(Qt.AlignCenter)
        self.answerBox.setObjectName("answerBox")
        self.verticalLayout_2.addWidget(self.answerBox)
        spacerItem3 = QSpacerItem(1503, 157, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.sortMode = QPushButton(Form)
        self.sortMode.setObjectName("sortMode")
        self.horizontalLayout_3.addWidget(self.sortMode)
        self.reviewMode = QPushButton(Form)
        self.reviewMode.setObjectName("reviewMode")
        self.horizontalLayout_3.addWidget(self.reviewMode)
        self.ignoreAnswer = QPushButton(Form)
        self.ignoreAnswer.setObjectName("ignoreAnswer")
        self.horizontalLayout_3.addWidget(self.ignoreAnswer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        self.rs = ReviewSession()
        self.promptLabel.setText( rs.current_review_queue["characters"] )
        # self.promptType.setText( rs.current_review_queue[""] )

        #self.sortMode.clicked.connect(  )
        # self.reviewMode.clicked.connect( rs.toggleReviewMode() )

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.percentCorrect.setText(_translate("Form", "Pct"))
        self.totalDone.setText(_translate("Form", "Done"))
        self.totalToDo.setText(_translate("Form", "Total"))
        self.promptLabel.setText(_translate("Form", "Prompt"))
        self.radicalCountToDo.setText(_translate("Form", "Rad: "))
        self.kanjiCountToDo.setText(_translate("Form", "Kan:"))
        self.vocabularyCountToDo.setText(_translate("Form", "Voc:"))
        self.promptType.setText(_translate("Form", "Prompt Type"))
        self.answerBox.setPlaceholderText(_translate("Form", "Answer"))
        self.sortMode.setText(_translate("Form", "Sort Mode"))
        self.reviewMode.setText(_translate("Form", "Anki Mode"))
        self.ignoreAnswer.setText(_translate("Form", "Ignore Answer"))

    def keyPressEvent( self, e ):
        if( type(e) == QKeyEvent ):
            if( e.key() == Qt.Key_Return ):
                self.answerBox.clear()
            else:
                super( ReviewWidget, self ).keyPressEvent(e)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = ReviewWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

