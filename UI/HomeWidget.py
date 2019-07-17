# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeScreenWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.Qt import *
from settings import Settings
from WK import HomepageStatsCategories, HomepageStatsListItems, Pages
from math import ceil

from WanikaniDatabase import WanikaniDatabase
from WanikaniLogoLabel import WanikaniLogoLabel
from ProgressionCircleLabel import ProgressionCircleLabel
from StatsListItemLabel import StatsListItemLabel

class HomeWidget( QWidget ):
    def __init__( self, MainWindow ):
        self.settings = Settings( Pages.HOME_PAGE )

        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi( self )

    def setupUi(self, Form ):
        Form.setObjectName("Form")

        self.homeWidgetVerticalLayout = QVBoxLayout(Form)
        self.homeWidgetVerticalLayout.setObjectName("verticalLayout_2")

        self.verticalLayoutMain = QVBoxLayout()
        self.verticalLayoutMain.setObjectName("verticalLayout")

        self.topBarHorizontalLayout = QHBoxLayout()
        self.topBarHorizontalLayout.setObjectName("topBarHorizontalLayout")

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.topBarHorizontalLayout.addItem(spacerItem)

        self.wanikaniLogo = WanikaniLogoLabel(Form)
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

        self.accountPushButton = QPushButton(Form)
        self.accountPushButton.setObjectName("pushButton")
        self.topBarHorizontalLayout.addWidget(self.accountPushButton)
        self.verticalLayoutMain.addLayout(self.topBarHorizontalLayout)

        self.searchBarHorizontalLayout = QHBoxLayout()
        self.searchBarHorizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.searchBarHorizontalLayout.setObjectName("searchBarHorizontalLayout")

        spacerItem2 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.searchBarHorizontalLayout.addItem(spacerItem2)

        self.searchBar = QLineEdit(Form)
        self.searchBar.setFrame(True)
        self.searchBar.setObjectName("searchBar")
        self.searchBarHorizontalLayout.addWidget(self.searchBar)
        self.verticalLayoutMain.addLayout(self.searchBarHorizontalLayout)

        self.availabilityHorizontalLayout = QHBoxLayout()
        self.availabilityHorizontalLayout.setObjectName("availabilityHorizontalLayout")

        self.nextReviewAvailable = QLabel(Form)
        self.nextReviewAvailable.setFrameShape(QFrame.Box)
        self.nextReviewAvailable.setAlignment(Qt.AlignCenter)
        self.nextReviewAvailable.setObjectName("nextReviewAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextReviewAvailable)

        self.nextHourAvailable = QLabel(Form)
        self.nextHourAvailable.setFrameShape(QFrame.Box)
        self.nextHourAvailable.setAlignment(Qt.AlignCenter)
        self.nextHourAvailable.setObjectName("nextHourAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextHourAvailable)

        self.nextDayAvailable = QLabel(Form)
        self.nextDayAvailable.setFrameShape(QFrame.Box)
        self.nextDayAvailable.setAlignment(Qt.AlignCenter)
        self.nextDayAvailable.setObjectName("nextDayAvailable")
        self.availabilityHorizontalLayout.addWidget(self.nextDayAvailable)
        self.verticalLayoutMain.addLayout(self.availabilityHorizontalLayout)

        self.subjectCountHorizontalLayout = QHBoxLayout()
        self.subjectCountHorizontalLayout.setObjectName("subjectCountHorizontalLayout")

        self.apprenticeCount = QLabel(Form)
        self.apprenticeCount.setFrameShape(QFrame.Box)
        self.apprenticeCount.setAlignment(Qt.AlignCenter)
        self.apprenticeCount.setObjectName("apprenticeCount")
        self.subjectCountHorizontalLayout.addWidget(self.apprenticeCount)

        self.guruCount = QLabel(Form)
        self.guruCount.setFrameShape(QFrame.Box)
        self.guruCount.setAlignment(Qt.AlignCenter)
        self.guruCount.setObjectName("guruCount")
        self.subjectCountHorizontalLayout.addWidget(self.guruCount)

        self.masterCount = QLabel(Form)
        self.masterCount.setFrameShape(QFrame.Box)
        self.masterCount.setTextFormat(Qt.AutoText)
        self.masterCount.setAlignment(Qt.AlignCenter)
        self.masterCount.setObjectName("masterCount")
        self.subjectCountHorizontalLayout.addWidget(self.masterCount)

        self.enlightenedCount = QLabel(Form)
        self.enlightenedCount.setFrameShape(QFrame.Box)
        self.enlightenedCount.setAlignment(Qt.AlignCenter)
        self.enlightenedCount.setObjectName("enlightenedCount")
        self.subjectCountHorizontalLayout.addWidget(self.enlightenedCount)

        self.burnedCount = QLabel(Form)
        self.burnedCount.setFrameShape(QFrame.Box)
        self.burnedCount.setAlignment(Qt.AlignCenter)
        self.burnedCount.setObjectName("burnedCount")
        self.subjectCountHorizontalLayout.addWidget(self.burnedCount)
        self.verticalLayoutMain.addLayout(self.subjectCountHorizontalLayout)

        self.levelRadicalVerticalLayout = QVBoxLayout()
        self.levelRadicalVerticalLayout.setObjectName("levelRadicalVerticalLayout")
        self.levelRadicalVerticalLayout.setContentsMargins(100, 0, 100, 0)

        self.levelRadicalProgressionLabel = QLabel(Form)
        self.levelRadicalProgressionLabel.setAlignment(Qt.AlignCenter)
        self.levelRadicalProgressionLabel.setObjectName("levelRadicalProgressionLabel")
        self.levelRadicalVerticalLayout.addWidget(self.levelRadicalProgressionLabel)

        self.levelRadicalProgressionItemsLocation = QHBoxLayout()
        self.levelRadicalProgressionItemsLocation.setObjectName("levelRadicalProgressionItemsLocation")
        self.levelRadicalProgressionItemsLocation.setSpacing( 0 )
        self.levelRadicalProgressionItemsLocation.setContentsMargins( 0,0,0,0 )
        self.levelRadicalVerticalLayout.addLayout(self.levelRadicalProgressionItemsLocation)
        self.verticalLayoutMain.addLayout(self.levelRadicalVerticalLayout)

        self.levelKanjiVerticalLayout = QVBoxLayout()
        self.levelKanjiVerticalLayout.setObjectName("levelKanjiVerticalLayout")
        self.levelKanjiVerticalLayout.setContentsMargins(100, 0, 100, 0)
        self.levelKanjiVerticalLayout.setSpacing(0)

        self.levelKanjiProgressionLabels = QLabel(Form)
        self.levelKanjiProgressionLabels.setAlignment(Qt.AlignCenter)
        self.levelKanjiProgressionLabels.setObjectName("levelKanjiProgressionLabels")
        self.levelKanjiVerticalLayout.addWidget(self.levelKanjiProgressionLabels)

        self.levelKanjiProgressionItemsLocation = QHBoxLayout()
        self.levelKanjiProgressionItemsLocation.setObjectName("levelKanjiProgressionItemsLocation")
        self.levelKanjiProgressionItemsLocation.setSpacing( 0 )
        self.levelKanjiProgressionItemsLocation.setContentsMargins( 0,0,0,0 )
        self.levelKanjiVerticalLayout.addLayout(self.levelKanjiProgressionItemsLocation)
        self.verticalLayoutMain.addLayout(self.levelKanjiVerticalLayout)

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
        self.verticalLayoutMain.addLayout(self.statsHorizontalLayout)

        # self.scrollArea = QScrollArea(Form)
        # self.scrollArea.setAutoFillBackground(False)
        # self.scrollArea.setWidgetResizable( True )
        # self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scrollArea.setAlignment(Qt.AlignCenter)
        # self.scrollArea.setObjectName("scrollArea")
        # self.mainScrollAreaWidgetContents = QWidget()
        # self.mainScrollAreaWidgetContents.setObjectName("mainScrollAreaWidgetContents")
        # self.mainScrollAreaWidgetContents.setContentsMargins(0,0,0,0)

        # self.scrollArea.setWidget(self.mainScrollAreaWidgetContents)
        # self.verticalLayoutMain.addWidget(self.scrollArea)

        self.homeWidgetVerticalLayout.addLayout(self.verticalLayoutMain)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        # Connect statement requires a callable function so dont put parentheses and if you must include parameters make it lambda
        self.reviewsLink.clicked.connect( lambda: self.MainWindow.openPage( Pages.REVIEW_PAGE ) )
        #self.lessonsLink.clicked.connect( self.setupLessonsScreen )
        #self.levelsLink.clicked.connect( self.setupLevelsScreeen )

        self.wk_db = WanikaniDatabase()
        """
        Assignment count diplay stuff
        """
        ap1Cnt = len( self.wk_db.getAssignmentsBySRSStageName( "Apprentice I" ) )
        ap2Cnt = len( self.wk_db.getAssignmentsBySRSStageName( "Apprentice II" ) )
        ap3Cnt = len( self.wk_db.getAssignmentsBySRSStageName( "Apprentice III" ) )
        ap4Cnt = len( self.wk_db.getAssignmentsBySRSStageName( "Apprentice IV" ) )
        self.apprenticeCount.setText( str( ap1Cnt + ap2Cnt + ap3Cnt + ap4Cnt ) )

        guru1Cnt = len( self.wk_db.getAssignmentsBySRSStageName( "Guru I" ) )
        guru2Cnt = len( self.wk_db.getAssignmentsBySRSStageName( "Guru II" ) )
        self.guruCount.setText( str( guru1Cnt + guru2Cnt ) )

        masterCnt = len( self.wk_db.getAssignmentsBySRSStageName( "Master" ) )
        self.masterCount.setText( str( masterCnt ) )

        enlightenedCnt = len( self.wk_db.getAssignmentsBySRSStageName( "Enlightened" ) )
        self.enlightenedCount.setText( str( enlightenedCnt ) )

        burnedCnt = len( self.wk_db.getAssignmentsBySRSStageName( "Burned" ) )
        self.burnedCount.setText( str(burnedCnt) )

        """
        Upcoming assignment display stuff
        """

        """
        Current level progression stuff
        """
        self.current_level = 57 #self.wk_db.getUserCurrentLevel()
        self.clr = self.wk_db.getSubjectObjectsOfGivenLevel( "radical", self.current_level )
        self.clk = self.wk_db.getSubjectObjectsOfGivenLevel( "kanji", self.current_level )

        self.getCLPINums()
        self.generateProgressionKanjiItems()
        self.generateProgressionRadicalItems()

        self.clpi_size_hint = self.size().width() / self.clk_layout_cutoff

        """
        Item stats stuff
        """
        self.statsHorizontalLayout.addStretch()
        self.MAX_STATS_ITEMS = 10

        # NEW UNLOCKS IN THE LAST 30 DAYS STUFF
        self.generateNewUnlocksList()

        self.statsHorizontalLayout.addStretch()

    def getCLPINums( self ):
        MAX_KANJI_IN_SINGLE_LEVEL = 42
        self.MAX_CLPI_ROW = ceil( MAX_KANJI_IN_SINGLE_LEVEL/2 )


    def generateProgressionRadicalItems( self ):
        # 34 is the largest number of radicals in a level, level 2
        self.current_level_radical_labels = []

        self.clr_layout_cutoff = self.MAX_CLPI_ROW # len( self.clr )

        if( len(self.clr) > self.clr_layout_cutoff ):
            self.levelRadicalProgressionItemsLocation2 = QHBoxLayout()
            self.levelRadicalProgressionItemsLocation2.setSpacing( 0 )
            self.levelRadicalProgressionItemsLocation2.setContentsMargins( 0,0,0,0 )
            self.levelRadicalVerticalLayout.addLayout( self.levelRadicalProgressionItemsLocation2 )

        self.levelRadicalProgressionItemsLocation.addStretch()

        for r in self.clr:
            r.getAssignmentInfo()

        self.clr = sorted(self.clr, key = lambda i: i.assignment.srs_stage )

        for index in range( len( self.clr ) ):
            # Create object, add it to the layout
            self.current_level_radical_labels.append( ProgressionCircleLabel(self, self.clr[index] ) )

            if( index < self.clr_layout_cutoff ):
                self.levelRadicalProgressionItemsLocation.addWidget( self.current_level_radical_labels[ index ] )

            else:
                if( index == self.clr_layout_cutoff ):
                    self.levelRadicalProgressionItemsLocation2.addStretch()

                self.levelRadicalProgressionItemsLocation2.addWidget( self.current_level_radical_labels[ index ], 0, Qt.AlignHCenter )

        self.levelRadicalProgressionItemsLocation.addStretch()

        if( len(self.clr) > self.clr_layout_cutoff ):
            self.levelRadicalProgressionItemsLocation2.addStretch()

    def generateProgressionKanjiItems( self ):
        # 42 is the largest number of kanji in a single level, in level 5
        self.current_level_kanji_labels = []
        self.clk_layout_cutoff = self.MAX_CLPI_ROW# len(self.clk)//2

        if( len(self.clk) > self.clk_layout_cutoff ):
            self.levelKanjiProgressionItemsLocation2 = QHBoxLayout()
            self.levelKanjiProgressionItemsLocation2.setSpacing( 0 )
            self.levelKanjiProgressionItemsLocation2.setContentsMargins( 0,0,0,0 )
            self.levelKanjiVerticalLayout.addLayout( self.levelKanjiProgressionItemsLocation2 )

        self.levelKanjiProgressionItemsLocation.addStretch()

        for k in self.clk:
            k.getAssignmentInfo()

        self.clk = sorted(self.clk, key = lambda i: i.assignment.srs_stage )

        for index in range( len( self.clk ) ):
            # Create object, add it to the layout
            self.current_level_kanji_labels.append( ProgressionCircleLabel(self, self.clk[index]) )

            if( index < self.clk_layout_cutoff ):
                self.levelKanjiProgressionItemsLocation.addWidget( self.current_level_kanji_labels[ index ] )

            else:
                if( index == self.clk_layout_cutoff ):
                    self.levelKanjiProgressionItemsLocation2.addStretch()

                self.levelKanjiProgressionItemsLocation2.addWidget( self.current_level_kanji_labels[ index ], 0, Qt.AlignHCenter )

        self.levelKanjiProgressionItemsLocation.addStretch()

        if( len(self.clk) > self.clk_layout_cutoff ):
            self.levelKanjiProgressionItemsLocation2.addStretch()

    def generateNewUnlocksList( self ):
        self.newUnlockTopLabel = StatsListItemLabel( self, HomepageStatsCategories.NEW_UNLOCKS, HomepageStatsListItems.TOP_LABEL )
        self.newUnlockLayout.addWidget( self.newUnlockTopLabel )

        # rua = recently unlocked assignments
        rua = self.wk_db.getRecentlyUnlockedAssignments()
        new_unlock_list_items = []
        # for i in range( self.MAX_STATS_ITEMS ):
            # # Add item to the new unlocks list
            # new_unlock_list_items.append( StatsListItemLabel( self, HomepageStatsCategories.NEW_UNLOCKS, rua[i] ) )

        self.newUnlockBottomLabel = StatsListItemLabel( self, HomepageStatsCategories.NEW_UNLOCKS, HomepageStatsListItems.BOTTOM_LABEL )
        self.newUnlockLayout.addWidget( self.newUnlockBottomLabel )

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
        self.accountPushButton.setText(_translate("Form", "Account"))
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
    ui = HomeWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

