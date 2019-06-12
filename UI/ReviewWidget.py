# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReviewPageTypingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.Qt import *
from settings import Settings
from ReviewSession import ReviewSession

from AnswerBox import AnswerBox
from ReviewPromptLabel import ReviewPromptLabel
from PromptTypeLabel import PromptTypeLabel

class ReviewWidget( QWidget ):
    def __init__(self, MainWindow):
        self.settings = Settings( "review_page" )
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

        self.homeButton = QPushButton("Home")
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_2.addWidget( self.homeButton )

        self.lightningButton = QPushButton("Z")
        self.lightningButton.setObjectName("lightningButton")
        self.horizontalLayout_2.addWidget( self.lightningButton )

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

        self.promptLabel = ReviewPromptLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setMinimumSize(QSize(0, 0))
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

        self.promptType = PromptTypeLabel(Form)
        self.promptType.setMinimumSize(QSize(0, 75))
        self.promptType.setAlignment(Qt.AlignCenter)
        self.promptType.setObjectName("promptType")
        self.verticalLayout_2.addWidget(self.promptType)

        self.answerBox = AnswerBox(Form)
        self.answerBox.setMinimumSize(QSize(0, 75))
        self.answerBox.setAlignment(Qt.AlignCenter)
        self.answerBox.setObjectName("answerBox")
        self.verticalLayout_2.addWidget(self.answerBox)

        self.ankiButtonsHorizontalLayout = QHBoxLayout()
        self.verticalLayout_2.addLayout( self.ankiButtonsHorizontalLayout )

        self.ankiYesButton = QPushButton(Form)
        self.ankiYesButton.setText( "Correct" )
        self.ankiYesButton.setMinimumSize(QSize(0,75))
        self.ankiYesButton.setObjectName("ankiYesButton")
        self.ankiButtonsHorizontalLayout.addWidget(self.ankiYesButton)
        self.ankiYesButton.setVisible(False)

        self.ankiNoButton = QPushButton(Form)
        self.ankiNoButton.setText( "Incorrect" )
        self.ankiNoButton.setMinimumSize(QSize(0,75))
        self.ankiNoButton.setObjectName("ankiNoButton")
        self.ankiButtonsHorizontalLayout.addWidget(self.ankiNoButton)
        self.ankiNoButton.setVisible(False)

        self.spacerItem3 = QSpacerItem(0, 157, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(self.spacerItem3)

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

        # This will later be loaded by a settings file
        # This can either be t for typing or a for anki
        self.review_mode = self.settings.settings["review_mode"]
        self.changeAnswerMode( self.review_mode )

        self.rs = ReviewSession()
        self.promptLabel.setText( self.rs.current_review_item["characters"] )
        self.promptType.setText( self.rs.current_question.capitalize() )
        self.promptType.setPromptStyle( self.rs.current_question )

        self.updateStats()

        self.homeButton.clicked.connect( lambda: self.changePage("home_page") )
        #self.sortMode.clicked.connect()
        self.reviewMode.clicked.connect( self.toggleAnswerMode )

        # Functions in connect statements must be callable so if you need to pass in arguments make it a lambda function
        self.ankiYesButton.clicked.connect( lambda: self.answerPrompt( True ) )
        self.ankiNoButton.clicked.connect( lambda: self.answerPrompt( False ) )


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

    def answerPrompt( self, boolean=None ):
        # Takes content from answer box if in typing mode else it takes the boolean its given
        answer_content = self.answerBox.text() if self.review_mode == "t" else boolean

        result = self.rs.answerCurrentQuestion( answer_content ,review_mode=self.review_mode )
        self.promptLabel.setText( self.rs.current_review_item["characters"] )
        self.promptType.setText( self.rs.current_question.capitalize() )
        self.promptType.setPromptStyle( self.rs.current_question )
        if( self.settings.settings["lightning"] ):                                                    # If lightning mode is enabled
            if( not result and self.settings.settings["delay_on_incorrect"] ):                        # Answer was wrong and delay on incorrect is enabled
                self.answerBox.setStyle("incorrect")
                # Start timer and check timer on enter and answer button presses to make sure it has passed
        else:
            if( result == True ):
                self.answerBox.setStyle( "correct" )
            else:
                self.answerBox.setStyle( "incorrect" )

        self.updateStats()
        # self.answerBox.clear()

    def updateStats( self ): # Result required to determine if question was answered correctly
        self.totalToDo.setText( str( self.rs.getTotalReviewsRemaining() ) )
        self.totalDone.setText( str( self.rs.total_done_reviews ) )
        self.percentCorrect.setText( str( self.rs.getPercentCorrectQuestions() ) + "%" )

    def changeAnswerMode( self, req = None ):
        if( req != None ):
            self.review_mode = req

        else:
            # Change mode from typing to anki and vice versa
            if( self.review_mode == "a" ):
                self.review_mode = "t"

            elif( self.review_mode == "t" ):
                self.review_mode = "a"

        if( self.review_mode == "a" ):
            # Subtracts 75 pixels for the minimum required for the anki buttons and 6 for the layouts margins
            self.spacerItem3.changeSize(0, 157 - 75 -6, QSizePolicy.Minimum, QSizePolicy.Preferred)

        elif( self.review_mode =="t" ):
            # Sets the spacers size back to default
            self.spacerItem3.changeSize(0, 157, QSizePolicy.Minimum, QSizePolicy.Preferred)

        is_anki_mode = self.review_mode == "a"
        self.ankiYesButton.setVisible( is_anki_mode )
        self.ankiNoButton.setVisible( is_anki_mode )
        self.answerBox.setReadOnly( is_anki_mode )

    def changePage( self, page ):
        # If page == None then we are exiting the application
        # Do settings saving if needed or anything else such as anything review related before exiting the page
        if( page != None ):
            self.MainWindow.openPage( page )

    def keyPressEvent( self, e ):
        if( type(e) == QKeyEvent ):
            if( e.key() == Qt.Key_Return ):
                self.answerPrompt()

        super( ReviewWidget, self ).keyPressEvent(e)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = ReviewWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

