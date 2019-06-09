from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from WanikaniSession import WanikaniSession
from WanikaniDatabase import WanikaniDatabase

import sys

class UI_MainWindow():
    def __init__( self ):
        self.app = QtWidgets.QApplication( [] )
        self.MainWindow = QtWidgets.QMainWindow()

        # MainWindow.setGeometry( 1000, 1000, 500, 500 )
        self.MainWindow.setWindowTitle("WanikaniPrototype")
        self.MainWindow.resize( 500, 500 )
        self.MainWindow.setObjectName("MainWindow")

        self.setupHomeScreen()

    def setupHomeScreen( self ):
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.topBarHorizontalLayout = QtWidgets.QHBoxLayout()
        self.topBarHorizontalLayout.setObjectName("topBarHorizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topBarHorizontalLayout.addItem(spacerItem)
        self.wanikaniLogo = QtWidgets.QLabel("Wanikani Logo")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wanikaniLogo.sizePolicy().hasHeightForWidth())

        self.wanikaniLogo.setSizePolicy(sizePolicy)
        self.wanikaniLogo.setMinimumSize(QtCore.QSize(0, 55))
        self.wanikaniLogo.setBaseSize(QtCore.QSize(0, 0))
        self.wanikaniLogo.setObjectName("wanikaniLogo")
        self.topBarHorizontalLayout.addWidget(self.wanikaniLogo)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topBarHorizontalLayout.addItem(spacerItem1)

        self.lessonsLink = QtWidgets.QPushButton( "Lessons" )
        self.lessonsLink.setObjectName("lessonsLink")
        self.topBarHorizontalLayout.addWidget(self.lessonsLink)

        self.reviewsLink = QtWidgets.QPushButton( "Reviews" )
        self.reviewsLink.setObjectName("reviewsLink")
        self.topBarHorizontalLayout.addWidget(self.reviewsLink)

        self.levelsLink = QtWidgets.QPushButton( "Levels" )
        self.levelsLink.setObjectName("levelsLink")
        self.topBarHorizontalLayout.addWidget(self.levelsLink)

        self.radicalLink = QtWidgets.QPushButton( "Radicals" )
        self.radicalLink.setObjectName("radicalLink")
        self.topBarHorizontalLayout.addWidget(self.radicalLink)

        self.kanjiLink = QtWidgets.QPushButton("Kanji")
        self.kanjiLink.setObjectName("kanjiLink")
        self.topBarHorizontalLayout.addWidget(self.kanjiLink)

        self.vocabularyLink = QtWidgets.QPushButton("Vocabulary")
        self.vocabularyLink.setObjectName("vocabularyLink")
        self.topBarHorizontalLayout.addWidget(self.vocabularyLink)

        self.accountLink = QtWidgets.QPushButton("Account")
        self.accountLink.setObjectName("pushButton")
        self.topBarHorizontalLayout.addWidget(self.accountLink)
        self.verticalLayout.addLayout(self.topBarHorizontalLayout)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")

        self.mainScrollAreaWidgetContents = QtWidgets.QWidget()
        self.mainScrollAreaWidgetContents.setObjectName("mainScrollAreaWidgetContents")

        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.mainScrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.verticalLayoutScrolling = QtWidgets.QVBoxLayout()
        self.verticalLayoutScrolling.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayoutScrolling.setObjectName("verticalLayoutScrolling")

        self.searchBarHorizontalLayout = QtWidgets.QHBoxLayout()
        self.searchBarHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.searchBarHorizontalLayout.setObjectName("searchBarHorizontalLayout")

        spacerItem2 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchBarHorizontalLayout.addItem(spacerItem2)

        self.searchBar = QtWidgets.QLineEdit(self.mainScrollAreaWidgetContents)
        self.searchBar.setFrame(True)
        self.searchBar.setObjectName("searchBar")
        self.searchBarHorizontalLayout.addWidget(self.searchBar)
        self.verticalLayoutScrolling.addLayout(self.searchBarHorizontalLayout)

        self.availabilityHorizontalLayout = QtWidgets.QHBoxLayout()
        self.availabilityHorizontalLayout.setObjectName("availabilityHorizontalLayout")

        self.nextReviewAvailable = QtWidgets.QLabel( "Next Review Available Time" )
        self.nextReviewAvailable.setFrameShape(QtWidgets.QFrame.Box)
        self.nextReviewAvailable.setAlignment(QtCore.Qt.AlignCenter)
        self.nextReviewAvailable.setObjectName("nextReviewAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextReviewAvailable)

        self.nextHourAvailable = QtWidgets.QLabel( "Available Next Hour" )
        self.nextHourAvailable.setFrameShape(QtWidgets.QFrame.Box)
        self.nextHourAvailable.setAlignment(QtCore.Qt.AlignCenter)
        self.nextHourAvailable.setObjectName("nextHourAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextHourAvailable)

        self.nextDayAvailable = QtWidgets.QLabel( "Available Next Day" )
        self.nextDayAvailable.setFrameShape(QtWidgets.QFrame.Box)
        self.nextDayAvailable.setAlignment(QtCore.Qt.AlignCenter)
        self.nextDayAvailable.setObjectName("nextDayAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextDayAvailable)

        self.verticalLayoutScrolling.addLayout(self.availabilityHorizontalLayout)

        self.subjectCountHorizontalLayout = QtWidgets.QHBoxLayout()
        self.subjectCountHorizontalLayout.setObjectName("subjectCountHorizontalLayout")

        self.apprenticeCount = QtWidgets.QLabel( "Apprentice Cnt" )
        self.apprenticeCount.setFrameShape(QtWidgets.QFrame.Box)
        self.apprenticeCount.setAlignment(QtCore.Qt.AlignCenter)
        self.apprenticeCount.setObjectName("apprenticeCount")
        self.subjectCountHorizontalLayout.addWidget(self.apprenticeCount)

        self.guruCount = QtWidgets.QLabel( "Guru Cnt" )
        self.guruCount.setFrameShape(QtWidgets.QFrame.Box)
        self.guruCount.setAlignment(QtCore.Qt.AlignCenter)
        self.guruCount.setObjectName("guruCount")
        self.subjectCountHorizontalLayout.addWidget(self.guruCount)

        self.masterCount = QtWidgets.QLabel("Master Cnt")
        self.masterCount.setFrameShape(QtWidgets.QFrame.Box)
        self.masterCount.setTextFormat(QtCore.Qt.AutoText)
        self.masterCount.setAlignment(QtCore.Qt.AlignCenter)
        self.masterCount.setObjectName("masterCount")
        self.subjectCountHorizontalLayout.addWidget(self.masterCount)

        self.enlightenedCount = QtWidgets.QLabel( "Enlightened Cnt" )
        self.enlightenedCount.setFrameShape(QtWidgets.QFrame.Box)
        self.enlightenedCount.setAlignment(QtCore.Qt.AlignCenter)
        self.enlightenedCount.setObjectName("enlightenedCount")
        self.subjectCountHorizontalLayout.addWidget(self.enlightenedCount)

        self.burnedCount = QtWidgets.QLabel( "Burned Cnt" )
        self.burnedCount.setFrameShape(QtWidgets.QFrame.Box)
        self.burnedCount.setAlignment(QtCore.Qt.AlignCenter)
        self.burnedCount.setObjectName("burnedCount")
        self.subjectCountHorizontalLayout.addWidget(self.burnedCount)

        self.verticalLayoutScrolling.addLayout(self.subjectCountHorizontalLayout)

        self.levelRadicalVerticalLayout = QtWidgets.QVBoxLayout()
        self.levelRadicalVerticalLayout.setObjectName("levelRadicalVerticalLayout")

        self.levelRadicalProgressionLabel = QtWidgets.QLabel( "Level Radical Progression" )
        self.levelRadicalProgressionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.levelRadicalProgressionLabel.setObjectName("levelRadicalProgressionLabel")
        self.levelRadicalVerticalLayout.addWidget(self.levelRadicalProgressionLabel)

        self.levelRadicalProgressionItemsLocation = QtWidgets.QHBoxLayout()
        self.levelRadicalProgressionItemsLocation.setObjectName("levelRadicalProgressionItemsLocation")
        self.levelRadicalVerticalLayout.addLayout(self.levelRadicalProgressionItemsLocation)

        self.verticalLayoutScrolling.addLayout(self.levelRadicalVerticalLayout)

        self.levelKanjiVerticalLayout = QtWidgets.QVBoxLayout()
        self.levelKanjiVerticalLayout.setObjectName("levelKanjiVerticalLayout")

        self.levelKanjiProgressionLabels = QtWidgets.QLabel( "Level Kanji Progression" )
        self.levelKanjiProgressionLabels.setAlignment(QtCore.Qt.AlignCenter)
        self.levelKanjiProgressionLabels.setObjectName("levelKanjiProgressionLabels")
        self.levelKanjiVerticalLayout.addWidget(self.levelKanjiProgressionLabels)

        self.levelKanjiProgressionItemsLocation = QtWidgets.QHBoxLayout()
        self.levelKanjiProgressionItemsLocation.setObjectName("levelKanjiProgressionItemsLocation")
        self.levelKanjiVerticalLayout.addLayout(self.levelKanjiProgressionItemsLocation)
        self.verticalLayoutScrolling.addLayout(self.levelKanjiVerticalLayout)

        self.statsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.statsHorizontalLayout.setObjectName("statsHorizontalLayout")

        self.newUnlockLayout = QtWidgets.QVBoxLayout()
        self.newUnlockLayout.setObjectName("newUnlockLayout")
        self.statsHorizontalLayout.addLayout(self.newUnlockLayout)

        self.criticalConditionLayout = QtWidgets.QVBoxLayout()
        self.criticalConditionLayout.setObjectName("criticalConditionLayout")
        self.statsHorizontalLayout.addLayout(self.criticalConditionLayout)

        self.burnedItemsLayout = QtWidgets.QVBoxLayout()
        self.burnedItemsLayout.setObjectName("burnedItemsLayout")
        self.statsHorizontalLayout.addLayout(self.burnedItemsLayout)

        self.verticalLayoutScrolling.addLayout(self.statsHorizontalLayout)
        self.verticalLayout_12.addLayout(self.verticalLayoutScrolling)

        self.scrollArea.setWidget(self.mainScrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        """
        Connect Methods
        """
        #self.lessonsLink.clicked.connect( self.setupLessonsScreen )
        self.reviewsLink.clicked.connect( self.setupReviewScreen )
        #self.levelsLink.clicked.connect( self.setupLevelsScreeen )
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def setupReviewScreen( self ):
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.percentCorrect = QtWidgets.QLabel("Pct")
        self.percentCorrect.setObjectName("percentCorrect")
        self.horizontalLayout_2.addWidget(self.percentCorrect)

        self.totalDone = QtWidgets.QLabel("Done")
        self.totalDone.setObjectName("totalDone")
        self.horizontalLayout_2.addWidget(self.totalDone)

        self.totalToDo = QtWidgets.QLabel("To Do")
        self.totalToDo.setObjectName("totalToDo")
        self.horizontalLayout_2.addWidget(self.totalToDo)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.promptLabel = QtWidgets.QLabel("Prompt")
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

        self.radicalCountToDo = QtWidgets.QLabel("Rad:")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radicalCountToDo.sizePolicy().hasHeightForWidth())
        self.radicalCountToDo.setSizePolicy(sizePolicy)
        self.radicalCountToDo.setMinimumSize(QtCore.QSize(40, 0))
        self.radicalCountToDo.setObjectName("radicalCountToDo")
        self.verticalLayout_3.addWidget(self.radicalCountToDo)

        self.kanjiCountToDo = QtWidgets.QLabel("Kan:")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kanjiCountToDo.sizePolicy().hasHeightForWidth())
        self.kanjiCountToDo.setSizePolicy(sizePolicy)
        self.kanjiCountToDo.setMinimumSize(QtCore.QSize(40, 0))
        self.kanjiCountToDo.setObjectName("kanjiCountToDo")
        self.verticalLayout_3.addWidget(self.kanjiCountToDo)

        self.vocabularyCountToDo = QtWidgets.QLabel("Voc:")
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

        self.promptType = QtWidgets.QLabel("Prompt Type")
        self.promptType.setMinimumSize(QtCore.QSize(0, 75))
        self.promptType.setAlignment(QtCore.Qt.AlignCenter)
        self.promptType.setObjectName("promptType")
        self.verticalLayout_2.addWidget(self.promptType)

        self.answerBox = QtWidgets.QLineEdit(self.centralwidget)
        self.answerBox.setMinimumSize(QtCore.QSize(0, 75))
        self.answerBox.setAlignment(QtCore.Qt.AlignCenter)
        self.answerBox.setObjectName("answerBox")
        self.verticalLayout_2.addWidget(self.answerBox)

        spacerItem3 = QtWidgets.QSpacerItem(20, 160, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)

        self.sortMode = QtWidgets.QPushButton("Sort Mode")
        self.sortMode.setObjectName("sortMode")
        self.horizontalLayout_3.addWidget(self.sortMode)

        self.reviewMode = QtWidgets.QPushButton("Review Mode")
        self.reviewMode.setObjectName("reviewMode")
        self.horizontalLayout_3.addWidget(self.reviewMode)

        self.ignoreAnswer = QtWidgets.QPushButton("Ignore Answer")
        self.ignoreAnswer.setObjectName("ignoreAnswer")
        self.horizontalLayout_3.addWidget(self.ignoreAnswer)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)


        """
        Connect Methods
        """
        self.sortMode.clicked.connect(self.centralwidget.hide)
        self.reviewMode.clicked.connect(self.centralwidget.hide)
        self.ignoreAnswer.clicked.connect(self.centralwidget.hide)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    def start( self ):
        self.MainWindow.show()
        sys.exit( self.app.exec_() )
