# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReviewPageAnkiAnswerNotShown.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 991)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.percentCorrect = QtWidgets.QLabel(self.centralwidget)
        self.percentCorrect.setObjectName("percentCorrect")
        self.horizontalLayout_2.addWidget(self.percentCorrect)
        self.totalDone = QtWidgets.QLabel(self.centralwidget)
        self.totalDone.setObjectName("totalDone")
        self.horizontalLayout_2.addWidget(self.totalDone)
        self.totalToDo = QtWidgets.QLabel(self.centralwidget)
        self.totalToDo.setObjectName("totalToDo")
        self.horizontalLayout_2.addWidget(self.totalToDo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.promptLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.promptLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.promptLabel.setLineWidth(3)
        self.promptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.promptLabel.setObjectName("promptLabel")
        self.horizontalLayout.addWidget(self.promptLabel)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radicalCountToDo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radicalCountToDo.sizePolicy().hasHeightForWidth())
        self.radicalCountToDo.setSizePolicy(sizePolicy)
        self.radicalCountToDo.setMinimumSize(QtCore.QSize(40, 0))
        self.radicalCountToDo.setObjectName("radicalCountToDo")
        self.verticalLayout_3.addWidget(self.radicalCountToDo)
        self.kanjiCountToDo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kanjiCountToDo.sizePolicy().hasHeightForWidth())
        self.kanjiCountToDo.setSizePolicy(sizePolicy)
        self.kanjiCountToDo.setMinimumSize(QtCore.QSize(40, 0))
        self.kanjiCountToDo.setObjectName("kanjiCountToDo")
        self.verticalLayout_3.addWidget(self.kanjiCountToDo)
        self.vocabularyCountToDo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vocabularyCountToDo.sizePolicy().hasHeightForWidth())
        self.vocabularyCountToDo.setSizePolicy(sizePolicy)
        self.vocabularyCountToDo.setMinimumSize(QtCore.QSize(40, 0))
        self.vocabularyCountToDo.setObjectName("vocabularyCountToDo")
        self.verticalLayout_3.addWidget(self.vocabularyCountToDo)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.promptType = QtWidgets.QLabel(self.centralwidget)
        self.promptType.setMinimumSize(QtCore.QSize(0, 75))
        self.promptType.setAlignment(QtCore.Qt.AlignCenter)
        self.promptType.setObjectName("promptType")
        self.verticalLayout_2.addWidget(self.promptType)
        self.answerBox = QtWidgets.QLineEdit(self.centralwidget)
        self.answerBox.setMinimumSize(QtCore.QSize(0, 75))
        self.answerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.answerBox.setObjectName("answerBox")
        self.verticalLayout_2.addWidget(self.answerBox)
        self.showAnswer = QtWidgets.QPushButton(self.centralwidget)
        self.showAnswer.setMinimumSize(QtCore.QSize(0, 75))
        self.showAnswer.setObjectName("showAnswer")
        self.verticalLayout_2.addWidget(self.showAnswer)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.sortMode = QtWidgets.QPushButton(self.centralwidget)
        self.sortMode.setObjectName("sortMode")
        self.horizontalLayout_3.addWidget(self.sortMode)
        self.reviewMode = QtWidgets.QPushButton(self.centralwidget)
        self.reviewMode.setObjectName("reviewMode")
        self.horizontalLayout_3.addWidget(self.reviewMode)
        self.ignoreAnswer = QtWidgets.QPushButton(self.centralwidget)
        self.ignoreAnswer.setObjectName("ignoreAnswer")
        self.horizontalLayout_3.addWidget(self.ignoreAnswer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1299, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.percentCorrect.setText(_translate("MainWindow", "Pct"))
        self.totalDone.setText(_translate("MainWindow", "Done"))
        self.totalToDo.setText(_translate("MainWindow", "Total"))
        self.promptLabel.setText(_translate("MainWindow", "Prompt"))
        self.radicalCountToDo.setText(_translate("MainWindow", "Rad: "))
        self.kanjiCountToDo.setText(_translate("MainWindow", "Kan:"))
        self.vocabularyCountToDo.setText(_translate("MainWindow", "Voc:"))
        self.promptType.setText(_translate("MainWindow", "Prompt Type"))
        self.answerBox.setPlaceholderText(_translate("MainWindow", "Answer"))
        self.showAnswer.setText(_translate("MainWindow", "Show Answer"))
        self.sortMode.setText(_translate("MainWindow", "Sort Mode"))
        self.reviewMode.setText(_translate("MainWindow", "Anki Mode"))
        self.ignoreAnswer.setText(_translate("MainWindow", "Ignore Answer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

