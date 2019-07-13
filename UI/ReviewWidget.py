# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReviewPageTypingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.Qt import *
from settings import Settings
from ReviewSession import ReviewSession
from WK import Pages, ReviewState, ReviewMode

from AnswerBox import AnswerBox
from ReviewPromptLabel import ReviewPromptLabel
from PromptTypeLabel import PromptTypeLabel
from LightningButton import LightningButton

class ReviewWidget( QWidget ):
    def __init__(self, MainWindow):
        self.settings = Settings( Pages.REVIEW_PAGE )
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi( self )

    def setupUi(self, Form):

        self.lightning = self.settings.settings["review_page"]["lightning"]
        self.delay_on_incorrect = self.settings.settings["review_page"]["delay_on_incorrect"]

        Form.setObjectName("Form")

        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.homeButton = QPushButton("Home")
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout_2.addWidget( self.homeButton )

        self.lightningButton = LightningButton( self.lightning )
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

        self.ankiShowAnswerButton = QPushButton(Form)
        self.ankiShowAnswerButton.setText( "Show Answer" )
        self.ankiShowAnswerButton.setMinimumSize(QSize(0,75))
        self.ankiShowAnswerButton.setObjectName("ankiShowAnswerButton")
        self.ankiButtonsHorizontalLayout.addWidget(self.ankiShowAnswerButton)
        self.ankiShowAnswerButton.hide()

        self.ankiYesButton = QPushButton(Form)
        self.ankiYesButton.setText( "Correct" )
        self.ankiYesButton.setMinimumSize(QSize(0,75))
        self.ankiYesButton.setObjectName("ankiYesButton")
        self.ankiButtonsHorizontalLayout.addWidget(self.ankiYesButton)
        self.ankiYesButton.hide()

        self.ankiNoButton = QPushButton(Form)
        self.ankiNoButton.setText( "Incorrect" )
        self.ankiNoButton.setMinimumSize(QSize(0,75))
        self.ankiNoButton.setObjectName("ankiNoButton")
        self.ankiButtonsHorizontalLayout.addWidget(self.ankiNoButton)
        self.ankiNoButton.hide()

        self.ankiNextQuestionButton = QPushButton(Form)
        self.ankiNextQuestionButton.setText( "Next Question" )
        self.ankiNextQuestionButton.setMinimumSize(QSize(0,75))
        self.ankiNextQuestionButton.setObjectName("ankiNextQuestionButton")
        self.ankiButtonsHorizontalLayout.addWidget(self.ankiNextQuestionButton)
        self.ankiNextQuestionButton.hide()

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
        self.review_mode = self.settings.settings["review_page"]["review_mode"]

        print( self.review_mode )

        self.setAnswerMode( self.review_mode )

        self.rs = ReviewSession()
        self.promptLabel.setText( self.rs.current_review_item.subject.characters )
        self.promptType.setText( self.rs.current_question.capitalize() )
        self.promptType.setPromptStyle( self.rs.current_question )

        # Updates the review stats in side bar
        self.updateStats()

        self.homeButton.clicked.connect( lambda: self.changePage(Pages.HOME_PAGE) )
        self.reviewMode.clicked.connect( self.toggleAnswerMode )

        # Functions in connect statements must be callable so
        # if you need to pass in arguments make it a lambda function
        self.ankiShowAnswerButton.clicked.connect( self.showAnswer )
        self.ankiYesButton.clicked.connect( lambda: self.answerPrompt( True ) )
        self.ankiNoButton.clicked.connect( lambda: self.answerPrompt( False ) )
        self.ankiNextQuestionButton.clicked.connect( self.nextReview )

        self.lightningButton.clicked.connect( self.toggleLightning )

        # Intializes delay on incorrect timer
        self.delayOnIncorrectTimer = QTimer()
        # self.delayOnIncorrectTimer.timout.connect( self.setAnswerGiven )

        self.setState(ReviewState.READY_FOR_ANSWER)

    def setState( self, state ):
        # Simply sets the current state of the review session to ANSWER GIVEN
        self.state = state
        print( "Current state: {}".format( self.state ) )

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

    def showAnswer( self  ):
        print( "Answer being shown..." )
        if( self.review_mode == ReviewMode.ANKI ):
            # Show answer buttons and hide the "show answer" button
            self.ankiShowAnswerButton.hide()
            self.ankiYesButton.show()
            self.ankiNoButton.show()

        # Show actual answer stuff here
        self.answerBox.setReadOnly( True )
        self.answerBox.setText( ", ".join( self.rs.getCorrectAnswer() ) )

        self.setState( ReviewState.ANSWER_SHOWN )

    def answerPrompt( self, boolean=None ):
        # Takes content from answer box if in typing mode else it takes the boolean its given
        answer_content = self.answerBox.text() if self.review_mode == ReviewMode.TYPING else boolean

        # Gets result from checking answer
        result = self.rs.answerCurrentQuestion( answer_content ,review_mode=self.review_mode )

        if( result == True ):
            self.setState( ReviewState.ANSWER_GIVEN )

            if( self.lightning ):  # If lightning mode is enabled
                self.nextReview()
                return

            else:
                self.answerBox.setStyle( "correct" )

        else:
            self.answerBox.setStyle( "incorrect" )
            if( self.delay_on_incorrect ):
                # Start timer for when you are allowed to move on to the next review item
                self.delayOnIncorrectTimer.singleShot( 1000, self.setAnswerGiven )
                self.setState( ReviewState.WAITING_FOR_INCORRECT_DELAY )

            else:
                self.setState( ReviewState.ANSWER_GIVEN )

        if( self.review_mode == ReviewMode.ANKI ):
            self.ankiYesButton.hide()
            self.ankiNoButton.hide()
            self.ankiNextQuestionButton.show()

        elif( self.review_mode == ReviewMode.TYPING ):
            self.answerBox.setReadOnly( True )

        self.updateStats()

    def nextReview( self ):
        if( self.state == ReviewState.ANSWER_GIVEN):
            # Sets prompt label to characters of the curent review item
            self.promptLabel.setText( self.rs.current_review_item.subject.characters )
            # Sets prompt type label to the character string representing the type of the question
            self.promptType.setText( self.rs.current_question.capitalize() )
            # Sets prompt type label to the style associated with the current question
            self.promptType.setPromptStyle( self.rs.current_question )
            # Clears the answer box for another answer
            self.answerBox.clear()

            # If we are reviewing in ankj mode
            if( self.review_mode == ReviewMode.ANKI ):
                # hide all buttons except show answer button
                self.ankiNoButton.hide()
                self.ankiYesButton.hide()
                self.ankiNextQuestionButton.hide()
                # Show the show answer button
                self.ankiShowAnswerButton.show()
            else:
                # If in typing mode remove the read only flag on the answer box
                self.answerBox.setReadOnly( False )

            # Set prompt type label back to default color
            self.answerBox.setStyle( "default" )

            # Set state to ready for next answer
            self.setState( ReviewState.READY_FOR_ANSWER )

        else:
            print( "Cannot get next review since current state is: {}".format( self.state ) )

    def updateStats( self ): # Result required to determine if question was answered correctly
        self.totalToDo.setText( str( self.rs.getTotalReviewsRemaining() ) )
        self.totalDone.setText( str( self.rs.total_done_reviews ) )
        self.percentCorrect.setText( str( self.rs.getPercentCorrectQuestions() ) + "%" )

    def toggleAnswerMode( self ):
        # Change mode from typing to anki and vice versa
        if( self.review_mode == ReviewMode.ANKI ):
            self.review_mode = ReviewMode.TYPING

        elif( self.review_mode == ReviewMode.TYPING ):
            self.review_mode = ReviewMode.ANKI

        self.changeAnswerModeAttributes()

    def setAnswerMode( self, mode ):
        # For changine answer mode to given value or cycling through them
        self.review_mode = mode

        # Change mode from typing to anki and vice versa
        if( self.review_mode == ReviewMode.ANKI ):
            self.review_mode = ReviewMode.TYPING

        elif( self.review_mode == ReviewMode.TYPING ):
            self.review_mode = ReviewMode.ANKI

        self.changeAnswerModeAttributes()

    def changeAnswerModeAttributes( self ):
        if( self.review_mode == ReviewMode.ANKI ):
            # Subtracts 75 pixels for the minimum required for the anki buttons and 6 for the layouts margins
            self.spacerItem3.changeSize(0, 157-75-6, QSizePolicy.Minimum, QSizePolicy.Preferred)

        elif( self.review_mode == ReviewMode.TYPING ):
            # Sets the spacers size back to default
            self.spacerItem3.changeSize(0, 157, QSizePolicy.Minimum, QSizePolicy.Preferred)

        is_anki_mode = self.review_mode == ReviewMode.ANKI
        self.ankiShowAnswerButton.setVisible( is_anki_mode )
        self.answerBox.setReadOnly( is_anki_mode )

    def toggleLightning( self ):
        if( self.lightning == False ):
            self.lightning = True

        else:
            self.lightning = False

        self.lightningButton.setLightning( self.lightning )

    def changePage( self, page ):
        # If page == None then we are exiting the application
        # Do settings saving if needed or anything else such as anything review related before exiting the page
        if( page != None ):
            self.MainWindow.openPage( page )

    def keyPressEvent( self, e ):
        if( type(e) == QKeyEvent ):
            if( e.key() == Qt.Key_Return ): # if the enter key is pressed:
                if( self.state == ReviewState.READY_FOR_ANSWER ):
                    self.answerPrompt()

                elif( self.state == ReviewState.ANSWER_GIVEN ):
                    self.nextReview()

                elif( self.state == ReviewState.WAITING_FOR_INCORRECT_DELAY ):
                    # Don't do anything if waiting for incorrect delay, the if statement
                    # isn't really necessary but i like it for continuity
                    pass

            elif( e.key() == Qt.Key_L and self.state == ReviewState.ANSWER_SHOWN ):
                self.answerPrompt( True )

            elif( e.key() == Qt.Key_Semicolon and self.state == ReviewState.ANSWER_SHOWN ):
                self.answerPrompt( False )

            elif( e.key() == Qt.Key_Apostrophe and self.state == ReviewState.READY_FOR_ANSWER ):
                self.showAnswer()

        super( ReviewWidget, self ).keyPressEvent(e)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = ReviewWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

