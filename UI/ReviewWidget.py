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
        self.settings = Settings()
        self.log = self.settings.logging
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi( self )

    def setupUi(self, Form):
        self.lightning = self.settings.settings["review_page"]["lightning"]
        self.delay_on_incorrect = self.settings.settings["review_page"]["delay_on_incorrect"]

        Form.setObjectName("Form")

        self.mainVLayout = QVBoxLayout(Form)
        self.mainVLayout.setObjectName("mainVLayout")

        self.topBarHLayout = QHBoxLayout()
        self.topBarHLayout.setObjectName("topBarHLayout")

        self.homeButton = QPushButton("Home")
        self.homeButton.setObjectName("homeButton")
        self.topBarHLayout.addWidget( self.homeButton )

        self.lightningButton = LightningButton( self.lightning )
        self.lightningButton.setObjectName("lightningButton")
        self.topBarHLayout.addWidget( self.lightningButton )

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.topBarHLayout.addItem(spacerItem)

        self.totalToDo = QLabel(Form)
        self.totalToDo.setObjectName("totalToDo")
        self.topBarHLayout.addWidget(self.totalToDo)

        self.totalDone = QLabel(Form)
        self.totalDone.setObjectName("totalDone")
        self.topBarHLayout.addWidget(self.totalDone)

        self.percentCorrect = QLabel(Form)
        self.percentCorrect.setObjectName("percentCorrect")
        self.topBarHLayout.addWidget(self.percentCorrect)

        self.mainVLayout.addLayout(self.topBarHLayout)

        self.promptAreaHLayout = QHBoxLayout()
        self.promptAreaHLayout.setObjectName("promptAreaHLayout")

        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.promptAreaHLayout.addItem(spacerItem1)

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
        self.promptAreaHLayout.addWidget(self.promptLabel)

        self.rightStatsBarVLayout = QVBoxLayout()
        self.rightStatsBarVLayout.setObjectName("rightStatsBarVLayout")

        self.radicalCountToDo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radicalCountToDo.sizePolicy().hasHeightForWidth())
        self.radicalCountToDo.setSizePolicy(sizePolicy)
        self.radicalCountToDo.setMinimumSize(QSize(40, 0))
        self.radicalCountToDo.setObjectName("radicalCountToDo")
        self.rightStatsBarVLayout.addWidget(self.radicalCountToDo)

        self.kanjiCountToDo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kanjiCountToDo.sizePolicy().hasHeightForWidth())
        self.kanjiCountToDo.setSizePolicy(sizePolicy)
        self.kanjiCountToDo.setMinimumSize(QSize(40, 0))
        self.kanjiCountToDo.setObjectName("kanjiCountToDo")
        self.rightStatsBarVLayout.addWidget(self.kanjiCountToDo)

        self.vocabularyCountToDo = QLabel(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vocabularyCountToDo.sizePolicy().hasHeightForWidth())
        self.vocabularyCountToDo.setSizePolicy(sizePolicy)
        self.vocabularyCountToDo.setMinimumSize(QSize(40, 0))
        self.vocabularyCountToDo.setObjectName("vocabularyCountToDo")
        self.rightStatsBarVLayout.addWidget(self.vocabularyCountToDo)

        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.rightStatsBarVLayout.addItem(spacerItem2)

        self.promptAreaHLayout.addLayout(self.rightStatsBarVLayout)
        self.mainVLayout.addLayout(self.promptAreaHLayout)

        self.promptType = PromptTypeLabel(Form)
        self.promptType.setMinimumSize(QSize(0, 75))
        self.promptType.setAlignment(Qt.AlignCenter)
        self.promptType.setObjectName("promptType")
        self.mainVLayout.addWidget(self.promptType)

        self.answerBox = AnswerBox(Form)
        self.answerBox.setMinimumSize(QSize(0, 75))
        self.answerBox.setAlignment(Qt.AlignCenter)
        self.answerBox.setObjectName("answerBox")
        self.mainVLayout.addWidget(self.answerBox)
        self.answerBox.setFocus()

        self.ankiButtonsHLayout = QHBoxLayout()
        self.mainVLayout.addLayout( self.ankiButtonsHLayout )

        self.ankiShowAnswerButton = QPushButton(Form)
        self.ankiShowAnswerButton.setText( "Show Answer" )
        self.ankiShowAnswerButton.setMinimumSize(QSize(0,75))
        self.ankiShowAnswerButton.setObjectName("ankiShowAnswerButton")
        self.ankiButtonsHLayout.addWidget(self.ankiShowAnswerButton)
        self.ankiShowAnswerButton.hide()

        self.ankiYesButton = QPushButton(Form)
        self.ankiYesButton.setText( "Correct" )
        self.ankiYesButton.setMinimumSize(QSize(0,75))
        self.ankiYesButton.setObjectName("ankiYesButton")
        self.ankiButtonsHLayout.addWidget(self.ankiYesButton)
        self.ankiYesButton.hide()

        self.ankiNoButton = QPushButton(Form)
        self.ankiNoButton.setText( "Incorrect" )
        self.ankiNoButton.setMinimumSize(QSize(0,75))
        self.ankiNoButton.setObjectName("ankiNoButton")
        self.ankiButtonsHLayout.addWidget(self.ankiNoButton)
        self.ankiNoButton.hide()

        self.ankiNextQuestionButton = QPushButton(Form)
        self.ankiNextQuestionButton.setText( "Next Question" )
        self.ankiNextQuestionButton.setMinimumSize(QSize(0,75))
        self.ankiNextQuestionButton.setObjectName("ankiNextQuestionButton")
        self.ankiButtonsHLayout.addWidget(self.ankiNextQuestionButton)
        self.ankiNextQuestionButton.hide()

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

        self.infoScrollArea = QScrollArea( Form )
        self.infoScrollArea.setAutoFillBackground(False)
        self.infoScrollArea.setWidgetResizable( True )
        self.infoScrollArea.setAlignment(Qt.AlignCenter)
        self.infoScrollArea.setObjectName("infoScrollArea")
        self.infoScrollAreaContents = QWidget()
        self.infoScrollAreaContents.setObjectName("mainScrollAreaWidgetContents")
        self.infoScrollAreaContents.setContentsMargins(0,0,0,0)

        self.infoScrollArea.setWidget(self.infoScrollAreaContents)
        self.mainVLayout.addWidget( self.infoScrollArea )
        self.infoScrollArea.hide()

        self.mainInfoHLayout = QHBoxLayout()
        self.infoScrollAreaContents.setLayout( self.mainInfoHLayout )
        self.leftVerticalLayout = QVBoxLayout()
        self.mainInfoHLayout.addLayout( self.leftVerticalLayout )
        self.rightVerticalLayout = QVBoxLayout()
        self.mainInfoHLayout.addLayout( self.rightVerticalLayout )

        self.bottomVerticalSpacer = QSpacerItem(0, 157, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.mainVLayout.addItem(self.bottomVerticalSpacer)

        self.extraButtonsHLayout = QHBoxLayout()
        self.extraButtonsHLayout.setObjectName("extraButtonsHLayout")

        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.extraButtonsHLayout.addItem(spacerItem4)

        self.sortMode = QPushButton(Form)
        self.sortMode.setObjectName("sortMode")
        self.extraButtonsHLayout.addWidget(self.sortMode)

        self.reviewMode = QPushButton(Form)
        self.reviewMode.setObjectName("reviewMode")
        self.extraButtonsHLayout.addWidget(self.reviewMode)

        self.ignoreAnswerButton = QPushButton(Form)
        self.ignoreAnswerButton.setObjectName("ignoreAnswerButton")
        self.extraButtonsHLayout.addWidget(self.ignoreAnswerButton)

        self.mainVLayout.addLayout(self.extraButtonsHLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        # This will later be loaded by a settings file
        # This can either be t for typing or a for anki
        self.review_mode = self.settings.settings["review_page"]["review_mode"]
        self.log.debug( "Review mode is now: {}".format( self.review_mode ) )

        self.setAnswerMode( self.review_mode )

        self.rs = ReviewSession()
        self.promptLabel.setText( self.rs.current_review_item.subject.characters )
        self.promptLabel.setStyle( self.rs.current_review_item.subject.object )
        self.promptType.setText( self.rs.current_question.capitalize() )
        self.promptType.setPromptStyle( self.rs.current_question )

        # Updates the review stats in side bar
        self.updateStats()

        self.homeButton.clicked.connect( lambda: self.changePage(Pages.HOME_PAGE) )
        self.reviewMode.clicked.connect( self.toggleAnswerMode )

        # Functions in connect statements must be callable so
        # if you need to pass in arguments make it a lambda function
        self.ankiShowAnswerButton.clicked.connect( self.showAnswerAnki )
        self.ankiYesButton.clicked.connect( lambda: self.answerPromptAnki( True ) )
        self.ankiNoButton.clicked.connect( lambda: self.answerPromptAnki( False ) )
        self.ankiNextQuestionButton.clicked.connect( self.nextReview )

        self.lightningButton.clicked.connect( self.toggleLightning )
        self.ignoreAnswerButton.clicked.connect( self.ignoreAnswer )

        # Intializes delay on incorrect timer
        self.delayOnIncorrectTimer = QTimer()
        # self.delayOnIncorrectTimer.timout.connect( self.setAnswerGiven )

        self.setState(ReviewState.READY_FOR_ANSWER)

    def setState( self, state ):
        # Simply sets the current state of the review session to ANSWER GIVEN
        self.review_state = state
        self.log.debug( "Current state: {}".format( self.review_state ) )

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
        self.ignoreAnswerButton.setText(_translate("Form", "Ignore Answer"))

    def showAnswerAnki( self  ):
        self.log.debug( "Answer being shown..." )
        if( self.review_mode == ReviewMode.ANKI ):
            # Show answer buttons and hide the "show answer" button
            self.ankiShowAnswerButton.hide()
            self.ankiYesButton.show()
            self.ankiNoButton.show()

        # Show actual answer stuff here
        self.answerBox.setReadOnly( True )
        self.answerBox.setText( ", ".join( self.rs.getCorrectAnswer() ) )

        self.setState( ReviewState.ANSWER_SHOWN )

    def ignoreAnswer( self ):
        # This resets the answer
        self.rs.resetLastAnswer()
        # This changes the style of the answerBox to show that it was ignored
        self.answerBox.setStyle("ignored")

    def answerPromptAnki( self, boolean ):
        # Gets result from checking answer
        result = self.rs.answerCurrentQuestionAnki( boolean )
        self.answerPrompt( result )

    def answerPromptTyping( self, text ):
        # Takes content from answer box if in typing mode else it takes the boolean its given
        result = self.rs.answerCurrentQuestionTyping( text )
        self.answerPrompt( result )

    def answerPrompt( self, result ):
        # Picks which answer prompt function to use based on truth value of result
        self.answerPromptTrue() if result else self.answerPromptFalse()
        # Hides answer buttons and shows next answer button if in anki mode and review state is ANSWER_GIVEN
        # Must check that answer given is mode since when lightning is on and result is true nextReview() is
        # called and changes review state to READY_FOR_ANSWER
        if( self.review_state == ReviewState.ANSWER_GIVEN ):
            if( self.review_mode == ReviewMode.ANKI ):
                self.ankiYesButton.hide()
                self.ankiNoButton.hide()
                self.ankiNextQuestionButton.show()

            elif( self.review_mode == ReviewMode.TYPING ):
                self.answerBox.setReadOnly( True )

        self.updateStats()

    def answerPromptTrue( self ):
        self.setState( ReviewState.ANSWER_GIVEN )
        if( self.lightning ):  # If lightning mode is enabled
            self.nextReview()
        else:
            self.answerBox.setStyle( "correct" )

    def answerPromptFalse( self ):
        self.answerBox.setStyle( "incorrect" )
        if( self.delay_on_incorrect ):
            # Start timer for when you are allowed to move on to the next review item
            self.delayOnIncorrectTimer.singleShot( 1000, self.setAnswerGiven )
            self.setState( ReviewState.WAITING_FOR_INCORRECT_DELAY )
        else:
            self.setState( ReviewState.ANSWER_GIVEN )

        if( self.lightning ):
            self.showPromptInfo()

    def nextReview( self ):
        if( self.review_state == ReviewState.ANSWER_GIVEN):
            self.rs.getNextReview()
            # Sets prompt label to characters of the curent review item and changes the color to the cooresponding subject type
            self.promptLabel.setText( self.rs.current_review_item.subject.characters )
            self.promptLabel.setStyle( self.rs.current_review_item.subject.object )
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

            # Hide info scroll area
            self.hidePromptInfo()

            # Set prompt type label back to default color
            self.answerBox.setStyle( "default" )

            # Set state to ready for next answer
            self.setState( ReviewState.READY_FOR_ANSWER )

        else:
            self.log.debug( "Cannot get next review since current state is: {}".format( self.review_state ) )

    def hidePromptInfo( self ):
        self.removePreviousItemPromptInfo()
        self.infoScrollArea.hide()
        # This effectively begins showing the spacer again since the hide() and show() methods don't work on spacer objects
        self.bottomVerticalSpacer.changeSize(0,157,QSizePolicy.Minimum, QSizePolicy.Preferred)

    def showPromptInfo( self ):
        subject = self.rs.current_review_item.subject.object

        if( subject == "kanji" ):
            self.createKanjiInfoContents()

        elif( subject == "vocabulary" ):
            self.createVocabularyInfoContents()

        self.infoScrollArea.show()
        # This effectivly hides the spacer since spacer objects cant use the hide() method
        self.bottomVerticalSpacer.changeSize(0,0,QSizePolicy.Ignored, QSizePolicy.Ignored)

    def createKanjiInfoContents( self ):
        if( self.rs.current_question == "meaning" ):
            self.meaningInfoLabel = QLabel( "Meanings: {}".format( self.rs.current_review_item.subject.getMeaningsString() ) )
            self.userSynonyms = QLabel( "User Synonyms" )
            self.radicalCombinations = QLabel( str(self.rs.current_review_item.subject.amalgamation_subject_ids ))
            self.meaningMnemonicLabel = QLabel( self.rs.current_review_item.subject.meaning_mnemonic )
            self.meaningHintLabel = QLabel( self.rs.current_review_item.subject.meaning_hint )
            self.meaningNote = QLabel( "Meaning Note" )

            self.leftVerticalLayout.addWidget( self.meaningInfoLabel )
            self.leftVerticalLayout.addWidget( self.userSynonyms )
            self.leftVerticalLayout.addWidget( self.radicalCombinations )
            self.rightVerticalLayout.addWidget( self.meaningMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.meaningHintLabel )
            self.rightVerticalLayout.addWidget( self.meaningNote )

        elif( self.rs.current_question == "reading" ):
            self.kunyomiLabel = QLabel( "Readings: {}".format( self.rs.current_review_item.subject.getReadingsString() ), self )
            self.radicalCombinations = QLabel( str(self.rs.current_review_item.subject.amalgamation_subject_ids ))
            self.readingMnemonicLabel = QLabel( self.rs.current_review_item.subject.reading_mnemonic )
            self.readingHintLabel = QLabel( self.rs.current_review_item.subject.reading_hint )
            self.readingNote = QLabel( "Reading Note" )

            self.leftVerticalLayout.addWidget( self.kunyomiLabel )
            self.leftVerticalLayout.addWidget( self.radicalCombinations )
            self.rightVerticalLayout.addWidget( self.readingMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.readingHintLabel )
            self.rightVerticalLayout.addWidget( self.readingNote )

    def createVocabularyInfoContents( self ):
        if( self.rs.current_question == "meaning" ):
            self.meaningInfoLabel = QLabel( "Meanings: {}".format( self.rs.current_review_item.subject.getMeaningsString() ), self )
            self.userSynonyms = QLabel( "User Synonyms" )
            self.partsOfSpeechLabel = QLabel( "Part of Speech: {}".format( self.rs.current_review_item.subject.getPartsOfSpeechString() ) )
            self.relatedKanji = QLabel( str(self.rs.current_review_item.subject.component_subject_ids ))
            self.meaningMnemonicLabel = QLabel( self.rs.current_review_item.subject.meaning_mnemonic )
            self.meaningNote = QLabel( "Meaning Note" )

            self.leftVerticalLayout.addWidget( self.meaningInfoLabel )
            self.leftVerticalLayout.addWidget( self.userSynonyms )
            self.leftVerticalLayout.addWidget( self.partsOfSpeechLabel )
            self.leftVerticalLayout.addWidget( self.relatedKanji )
            self.rightVerticalLayout.addWidget( self.meaningMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.meaningNote )

        elif( self.rs.current_question == "reading" ):
            self.readingInfoLabel = QLabel( "Readings: {}".format( self.rs.current_review_item.subject.getReadingsString() ), self)
            self.partsOfSpeechLabel = QLabel( "Part of Speech: {}".format( self.rs.current_review_item.subject.getPartsOfSpeechString() ) )
            self.relatedKanji = QLabel( str(self.rs.current_review_item.subject.component_subject_ids ))
            self.readingMnemonicLabel = QLabel( self.rs.current_review_item.subject.reading_mnemonic )
            self.readingNote = QLabel( "Reading Note" )

            self.leftVerticalLayout.addWidget( self.readingInfoLabel )
            self.leftVerticalLayout.addWidget( self.partsOfSpeechLabel )
            self.leftVerticalLayout.addWidget( self.relatedKanji )
            self.rightVerticalLayout.addWidget( self.readingMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.readingNote )

    def removePreviousItemPromptInfo( self ):
        for layout in [ self.leftVerticalLayout, self.rightVerticalLayout ]:
            for i in range( layout.count() ):
                obj = layout.takeAt( 0 ) # Removes the first object and puts it in obj, all other objects in layout are shifted down
                obj.widget().setVisible( False )
                obj = obj.widget() # del says it cant delete a function call so this must be done
                del obj

    def updateStats( self ): # Result required to determine if question was answered correctly
        self.totalToDo.setText( "Total: {}".format( self.rs.getTotalReviewsRemaining() ) )
        self.totalDone.setText( "Done: {}".format( self.rs.total_done_reviews ) )
        self.percentCorrect.setText( "Correct: {:>6.2f}%".format( self.rs.getPercentCorrectQuestions() ) )
        self.radicalCountToDo.setText( "R: {}".format( self.rs.getRadicalCount() ) )
        self.kanjiCountToDo.setText( "K: {}".format( self.rs.getKanjiCount() ) )
        self.vocabularyCountToDo.setText( "V: {}".format( self.rs.getVocabularyCount() ) )

    def toggleAnswerMode( self ):
        # Change mode from typing to anki and vice versa
        if( self.review_mode == ReviewMode.ANKI ):
            self.review_mode = ReviewMode.TYPING

        elif( self.review_mode == ReviewMode.TYPING ):
            self.review_mode = ReviewMode.ANKI

        self.log.debug("Changing review mode to {}".format( self.review_mode ))
        self.changeAnswerModeAttributes()

    def setAnswerMode( self, mode ):
        # For changing answer mode to given value or cycling through them
        self.review_mode = mode

        # Change mode from typing to anki and vice versa
        if( self.review_mode == ReviewMode.ANKI ):
            self.review_mode = ReviewMode.TYPING

        elif( self.review_mode == ReviewMode.TYPING ):
            self.review_mode = ReviewMode.ANKI

        self.log.debug("Changing review mode to {}".format( self.review_mode ))
        self.changeAnswerModeAttributes()

    def changeAnswerModeAttributes( self ):
        if( self.review_mode == ReviewMode.ANKI ):
            # Subtracts 75 pixels for the minimum required for the anki buttons and 6 for the layouts margins
            self.bottomVerticalSpacer.changeSize(0, 157-75-6, QSizePolicy.Minimum, QSizePolicy.Preferred)

        elif( self.review_mode == ReviewMode.TYPING ):
            # Sets the spacers size back to default
            self.bottomVerticalSpacer.changeSize(0, 157, QSizePolicy.Minimum, QSizePolicy.Preferred)

        is_anki_mode = self.review_mode == ReviewMode.ANKI
        self.ankiShowAnswerButton.setVisible( is_anki_mode )
        self.answerBox.setReadOnly( is_anki_mode )

    def toggleLightning( self ):
        if( self.lightning == False ):
            self.lightning = True
        else:
            self.lightning = False

        self.log.debug("Changing lightning button status to {}".format(self.lightning))
        self.lightningButton.setLightning( self.lightning )

    def changePage( self, page ):
        # If page == None then we are exiting the application
        # Do settings saving if needed or anything else such as anything review related before exiting the page
        if( page != None ):
            self.log.debug( "Changing page to {}".format( page ) )
            self.MainWindow.openPage( page )

    def keyPressEvent( self, e ):
        if( type(e) == QKeyEvent ):
            if( e.key() == Qt.Key_Return ): # if the enter key is pressed:
                if( self.review_state == ReviewState.READY_FOR_ANSWER ):
                    self.answerPromptTyping( self.answerBox.text() ) if self.review_mode == ReviewMode.TYPING else None

                elif( self.review_state == ReviewState.ANSWER_GIVEN ):
                    self.nextReview()

                elif( self.review_state == ReviewState.WAITING_FOR_INCORRECT_DELAY ):
                    # Don't do anything if waiting for incorrect delay, the if statement
                    # isn't really necessary but i like it for continuity
                    pass

            elif( e.key() == Qt.Key_L and self.review_state == ReviewState.ANSWER_SHOWN ):
                self.answerPromptAnki( True )

            elif( e.key() == Qt.Key_Semicolon and self.review_state == ReviewState.ANSWER_SHOWN ):
                self.answerPromptAnki( False )

            elif( e.key() == Qt.Key_Apostrophe and self.review_state == ReviewState.READY_FOR_ANSWER ):
                self.showAnswerAnki()

        super( ReviewWidget, self ).keyPressEvent(e)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = ReviewWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
