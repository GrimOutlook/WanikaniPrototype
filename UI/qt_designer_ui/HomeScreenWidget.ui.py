# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeScreenWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.Qt import *

class Ui_Form( QWidget ):
    def __init__( self, MainWindow ):
        QWidget.__init__(self)
        self.setupUi( self, MainWindow )

    def setupUi(self, Form, MainWindow):
        Form.setObjectName("Form")
        Form.resize(1118, 666)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.topBarHorizontalLayout = QHBoxLayout()
        self.topBarHorizontalLayout.setObjectName("topBarHorizontalLayout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.topBarHorizontalLayout.addItem(spacerItem)
        self.wanikaniLogo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wanikaniLogo.sizePolicy().hasHeightForWidth())
        self.wanikaniLogo.setSizePolicy(sizePolicy)
        self.wanikaniLogo.setMinimumSize(QSize(0, 55))
        self.wanikaniLogo.setBaseSize(QSize(0, 0))
        self.wanikaniLogo.setObjectName("wanikaniLogo")
        self.topBarHorizontalLayout.addWidget(self.wanikaniLogo)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.topBarHorizontalLayout.addItem(spacerItem1)
        self.lessonsLink = QPushButton(Form)
        self.lessonsLink.setObjectName("lessonsLink")
        self.topBarHorizontalLayout.addWidget(self.lessonsLink)
        self.reviewsLink = QPushButton(Form)
        self.reviewsLink.setObjectName("reviewsLink")
        self.topBarHorizontalLayout.addWidget(self.reviewsLink)
        self.levelsLink = QPushButton(Form)
        self.levelsLink.setObjectName("levelsLink")
        self.topBarHorizontalLayout.addWidget(self.levelsLink)
        self.radicalLink = QPushButton(Form)
        self.radicalLink.setObjectName("radicalLink")
        self.topBarHorizontalLayout.addWidget(self.radicalLink)
        self.kanjiLink = QPushButton(Form)
        self.kanjiLink.setObjectName("kanjiLink")
        self.topBarHorizontalLayout.addWidget(self.kanjiLink)
        self.vocabularyLink = QPushButton(Form)
        self.vocabularyLink.setObjectName("vocabularyLink")
        self.topBarHorizontalLayout.addWidget(self.vocabularyLink)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.topBarHorizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.topBarHorizontalLayout)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.mainScrollAreaWidgetContents = QWidget()
        self.mainScrollAreaWidgetContents.setGeometry(QRect(0, 0, 1096, 581))
        self.mainScrollAreaWidgetContents.setObjectName("mainScrollAreaWidgetContents")
        self.verticalLayout_12 = QVBoxLayout(self.mainScrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayoutScrolling = QVBoxLayout()
        self.verticalLayoutScrolling.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayoutScrolling.setObjectName("verticalLayoutScrolling")
        self.searchBarHorizontalLayout = QHBoxLayout()
        self.searchBarHorizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.searchBarHorizontalLayout.setObjectName("searchBarHorizontalLayout")
        spacerItem2 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.searchBarHorizontalLayout.addItem(spacerItem2)
        self.searchBar = QLineEdit(self.mainScrollAreaWidgetContents)
        self.searchBar.setFrame(True)
        self.searchBar.setObjectName("searchBar")
        self.searchBarHorizontalLayout.addWidget(self.searchBar)
        self.verticalLayoutScrolling.addLayout(self.searchBarHorizontalLayout)
        self.availabilityHorizontalLayout = QHBoxLayout()
        self.availabilityHorizontalLayout.setObjectName("availabilityHorizontalLayout")
        self.nextReviewAvailable = QLabel(self.mainScrollAreaWidgetContents)
        self.nextReviewAvailable.setFrameShape(QFrame.Box)
        self.nextReviewAvailable.setAlignment(Qt.AlignCenter)
        self.nextReviewAvailable.setObjectName("nextReviewAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextReviewAvailable)
        self.nextHourAvailable = QLabel(self.mainScrollAreaWidgetContents)
        self.nextHourAvailable.setFrameShape(QFrame.Box)
        self.nextHourAvailable.setAlignment(Qt.AlignCenter)
        self.nextHourAvailable.setObjectName("nextHourAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextHourAvailable)
        self.nextDayAvailable = QLabel(self.mainScrollAreaWidgetContents)
        self.nextDayAvailable.setFrameShape(QFrame.Box)
        self.nextDayAvailable.setAlignment(Qt.AlignCenter)
        self.nextDayAvailable.setObjectName("nextDayAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextDayAvailable)
        self.verticalLayoutScrolling.addLayout(self.availabilityHorizontalLayout)
        self.subjectCountHorizontalLayout = QHBoxLayout()
        self.subjectCountHorizontalLayout.setObjectName("subjectCountHorizontalLayout")
        self.apprenticeCount = QLabel(self.mainScrollAreaWidgetContents)
        self.apprenticeCount.setFrameShape(QFrame.Box)
        self.apprenticeCount.setAlignment(Qt.AlignCenter)
        self.apprenticeCount.setObjectName("apprenticeCount")
        self.subjectCountHorizontalLayout.addWidget(self.apprenticeCount)
        self.guruCount = QLabel(self.mainScrollAreaWidgetContents)
        self.guruCount.setFrameShape(QFrame.Box)
        self.guruCount.setAlignment(Qt.AlignCenter)
        self.guruCount.setObjectName("guruCount")
        self.subjectCountHorizontalLayout.addWidget(self.guruCount)
        self.masterCount = QLabel(self.mainScrollAreaWidgetContents)
        self.masterCount.setFrameShape(QFrame.Box)
        self.masterCount.setTextFormat(Qt.AutoText)
        self.masterCount.setAlignment(Qt.AlignCenter)
        self.masterCount.setObjectName("masterCount")
        self.subjectCountHorizontalLayout.addWidget(self.masterCount)
        self.enlightenedCount = QLabel(self.mainScrollAreaWidgetContents)
        self.enlightenedCount.setFrameShape(QFrame.Box)
        self.enlightenedCount.setAlignment(Qt.AlignCenter)
        self.enlightenedCount.setObjectName("enlightenedCount")
        self.subjectCountHorizontalLayout.addWidget(self.enlightenedCount)
        self.burnedCount = QLabel(self.mainScrollAreaWidgetContents)
        self.burnedCount.setFrameShape(QFrame.Box)
        self.burnedCount.setAlignment(Qt.AlignCenter)
        self.burnedCount.setObjectName("burnedCount")
        self.subjectCountHorizontalLayout.addWidget(self.burnedCount)
        self.verticalLayoutScrolling.addLayout(self.subjectCountHorizontalLayout)
        self.levelRadicalVerticalLayout = QVBoxLayout()
        self.levelRadicalVerticalLayout.setObjectName("levelRadicalVerticalLayout")
        self.levelRadicalProgressionLabel = QLabel(self.mainScrollAreaWidgetContents)
        self.levelRadicalProgressionLabel.setAlignment(Qt.AlignCenter)
        self.levelRadicalProgressionLabel.setObjectName("levelRadicalProgressionLabel")
        self.levelRadicalVerticalLayout.addWidget(self.levelRadicalProgressionLabel)
        self.levelRadicalProgressionItemsLocation = QHBoxLayout()
        self.levelRadicalProgressionItemsLocation.setObjectName("levelRadicalProgressionItemsLocation")
        self.levelRadicalVerticalLayout.addLayout(self.levelRadicalProgressionItemsLocation)
        self.verticalLayoutScrolling.addLayout(self.levelRadicalVerticalLayout)
        self.levelKanjiVerticalLayout = QVBoxLayout()
        self.levelKanjiVerticalLayout.setObjectName("levelKanjiVerticalLayout")
        self.levelKanjiProgressionLabels = QLabel(self.mainScrollAreaWidgetContents)
        self.levelKanjiProgressionLabels.setAlignment(Qt.AlignCenter)
        self.levelKanjiProgressionLabels.setObjectName("levelKanjiProgressionLabels")
        self.levelKanjiVerticalLayout.addWidget(self.levelKanjiProgressionLabels)
        self.levelKanjiProgressionItemsLocation = QHBoxLayout()
        self.levelKanjiProgressionItemsLocation.setObjectName("levelKanjiProgressionItemsLocation")
        self.levelKanjiVerticalLayout.addLayout(self.levelKanjiProgressionItemsLocation)
        self.verticalLayoutScrolling.addLayout(self.levelKanjiVerticalLayout)
        self.statsHorizontalLayout = QHBoxLayout()
        self.statsHorizontalLayout.setObjectName("statsHorizontalLayout")
        self.newUnlockLayout = QVBoxLayout()
        self.newUnlockLayout.setObjectName("newUnlockLayout")
        self.statsHorizontalLayout.addLayout(self.newUnlockLayout)
        self.criticalConditionLayout = QVBoxLayout()
        self.criticalConditionLayout.setObjectName("criticalConditionLayout")
        self.statsHorizontalLayout.addLayout(self.criticalConditionLayout)
        self.burnedItemsLayout = QVBoxLayout()
        self.burnedItemsLayout.setObjectName("burnedItemsLayout")
        self.statsHorizontalLayout.addLayout(self.burnedItemsLayout)
        self.verticalLayoutScrolling.addLayout(self.statsHorizontalLayout)
        self.verticalLayout_12.addLayout(self.verticalLayoutScrolling)
        self.scrollArea.setWidget(self.mainScrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        self.reviewsLink.clicked.connect( MainWindow.openReviews() )
        #self.lessonsLink.clicked.connect( self.setupLessonsScreen )
        #self.levelsLink.clicked.connect( self.setupLevelsScreeen )


    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.wanikaniLogo.setText(_translate("Form", "WaniKani Logo"))
        self.lessonsLink.setText(_translate("Form", "Lessons"))
        self.reviewsLink.setText(_translate("Form", "Reviews"))
        self.levelsLink.setText(_translate("Form", "Levels"))
        self.radicalLink.setText(_translate("Form", "Radicals"))
        self.kanjiLink.setText(_translate("Form", "Kanji"))
        self.vocabularyLink.setText(_translate("Form", "Vocabulary"))
        self.pushButton.setText(_translate("Form", "Account"))
        self.nextReviewAvailable.setText(_translate("Form", "Next Review Available"))
        self.nextHourAvailable.setText(_translate("Form", "Available Next Hour"))
        self.nextDayAvailable.setText(_translate("Form", "Available Next Day"))
        self.apprenticeCount.setText(_translate("Form", "Apprentice Cnt"))
        self.guruCount.setText(_translate("Form", "Guru Cnt"))
        self.masterCount.setText(_translate("Form", "Master Cnt"))
        self.enlightenedCount.setText(_translate("Form", "Enlightened Cnt"))
        self.burnedCount.setText(_translate("Form", "Burned Cnt"))
        self.levelRadicalProgressionLabel.setText(_translate("Form", "Level Radical Progression"))
        self.levelKanjiProgressionLabels.setText(_translate("Form", "Level Kanji Progression"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

