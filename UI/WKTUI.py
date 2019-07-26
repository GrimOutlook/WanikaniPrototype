import curses, sys, time
sys.path.append("..")
sys.path.append("../WK")

from settings import Settings
from WanikaniSession import WanikaniSession
from ReviewSession import ReviewSession
from WK import ReviewMode, ReviewState, TerminalColorPalette, TerminalColors
from PseudoJapaneseIME import PseudoJapaneseIME

"""
Probably need to check if necessary fonts are installed for language
"""
class WKTUI():
    def __init__( self ):
        try:
            self.settings = Settings()
            self.log = self.settings.logging

            self.log.debug( 'WKTUI Started Initializing.' )

            curses.setupterm("xterm-256color")
            self.scr = curses.initscr()
            self.scr.border()
            curses.cbreak()
            self.scr.keypad(False)
            curses.noecho()

            curses.start_color()
            # curses.init_pair( TerminalColors.DEFAULT, curses.COLOR_CYAN, curses.COLOR_WHITE)
            # curses.init_pair( 2, curses.COLOR_RED, curses.COLOR_WHITE)
            curses.init_pair( TerminalColorPalette.DEFAULT_HIGHLIGHT, curses.COLOR_BLACK, curses.COLOR_WHITE)               # Default highlight
            curses.init_pair( TerminalColorPalette.CORRECT_ANSWER_BOX, curses.COLOR_BLACK, TerminalColors.CORRECT_GREEN)    # Correct
            curses.init_pair( TerminalColorPalette.INCORRECT_ANSWER_BOX, curses.COLOR_WHITE, TerminalColors.INCORRECT_RED)  # Incorrect
            curses.init_pair( TerminalColorPalette.IGNORED_ANSWER_BOX, curses.COLOR_WHITE, TerminalColors.IGNORED_YELLOW)   # Ignored
            curses.init_pair( TerminalColorPalette.MEANING_QUESTION, curses.COLOR_BLACK, TerminalColors.MEANING_WHITE)      # Meaning Question Color
            curses.init_pair( TerminalColorPalette.READING_QUESTION, curses.COLOR_WHITE, TerminalColors.READING_BLACK)      # Reading Question Color
            curses.init_pair( TerminalColorPalette.REVIEW_VOCABULARY, curses.COLOR_WHITE, TerminalColors.VOCABULARY_PURPLE) # Vocab Color
            curses.init_pair( TerminalColorPalette.REVIEW_KANJI, curses.COLOR_WHITE, TerminalColors.KANJI_PINK)             # Kanji Color

            self.height, self.width = self.scr.getmaxyx()

            self.rs = ReviewSession()
            self.rs.setSortMode([["Subject","A"],["Level","A"]])
            self.IME = PseudoJapaneseIME()

            # Get default from settings here
            self.log.debug("Setting review modes")
            self.setAnswerBoxColorscheme( TerminalColorPalette.DEFAULT_HIGHLIGHT )
            self.review_mode = ReviewMode.ANKI
            self.review_state = ReviewState.READY_FOR_ANSWER
            self.delay_on_incorrect = True
            self.DELAY_TIME = 1 # 1 Second
            self.incorrect_start_time = 0
            self.lightning = False
            self.text = ""
            self.info_section_visible = False

            self.log.debug( "Setting char values" )
            BACKSPACE_CHAR = ord( "\x7f" )
            self.bad_chars = [  None, BACKSPACE_CHAR, ord("~"), ord("`"), ord("\n"), ord('!'),
                                curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT ]
            self.log.debug( 'WKTUI Finished Initializing.' )

        except Exception as e:
            self.log.exception( 'Exception occured during initialization of WKTUI.', exc_info=True )
            curses.endwin()
            print( e )

    def drawReviewScreen( self ):
        self.log.debug("Drawing review screen")
        try:
            ch = None

            while( ch != ord("~") ):
                # Get blank canvas
                self.scr.clear()
                self.height, self.width = self.scr.getmaxyx()

                self.handleKey( ch )

                self.drawSubjectType()
                self.drawKanji()
                self.drawTopStatsBar()
                self.drawStatusBar()

                if( self.info_section_visible ):
                    self.drawReviewInfoSection()

                self.drawQuestionType()
                self.drawAnswerBox( self.text )

                # Refresh screen
                self.scr.refresh()
                # Wait for next input
                ch = self.scr.getch()

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawReviewScreen.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawReviewScreen.', exc_info=True )
            curses.endwin()
            print( e )

    def toggleReviewMode( self ):
        self.review_mode = ReviewMode.ANKI if self.review_mode == ReviewMode.TYPING else ReviewMode.TYPING

    def setState( self, state ):
        self.review_state = state
        self.log.debug( "ReviewState is now {}".format( self.review_state ) )

    def clearText( self ):
        self.text = ""

    def handleKey( self, ch ):
        self.log.debug( "Key pressed: {}".format( ch ) )
        if ch == None: return

        # This is where keys that have effect during any state go
        if( ch == ord('!') ):
            self.rs.resetLastAnswer()
            self.setAnswerBoxColorscheme( TerminalColorPalette.IGNORED_ANSWER_BOX )
        elif( ch == ord('`') ):
            self.toggleReviewMode()

        # This is where keys that have effect in context of certain states go
        if( self.review_state == ReviewState.READY_FOR_ANSWER ):
            self.handleKeyReadyForAnswer( ch )
        elif( self.review_state == ReviewState.ANSWER_SHOWN ):
            self.handleKeyAnswerShown( ch )
        elif( self.review_state == ReviewState.ANSWER_GIVEN ):
            self.handleKeyAnswerGiven( ch )
        elif( self.review_state == ReviewState.WAITING_FOR_INCORRECT_DELAY ):
            self.handleKeyWaitingForDelay( ch )

    def handleKeyReadyForAnswer( self, ch ):
        if( self.review_mode == ReviewMode.TYPING and ch not in self.bad_chars ):
            self.text += chr( ch )
            if( self.rs.current_question == "reading" ):
                new_text = self.IME.romanjiToKana( self.text )
                self.text = new_text
        # This is the backspace key, currently hacked together since curses.KEY_BACKSPACE doesn't work
        elif( ch == ord('\x7f') ):
            self.text = self.text[:-1]
        # This is the enter key
        elif( ch == ord('\n') and self.text != "" ):
            self.answerReviewTyping( self.text )

        elif( self.review_mode == ReviewMode.ANKI and ch not in self.bad_chars ):
            if( ch == ord('3') ): # This key is used to show answer in anki mode
                self.showAnswer()

    def handleKeyAnswerShown( self, ch ):
        if( ch == ord('1') ): # This is the number 1 key, used for correct answer in anki mode
            self.answerReviewAnki( True )
        elif( ch == ord('2') ): # This is the number 2 key, used for incorrect answer in anki mode
            self.answerReviewAnki( False ) # False because incorrect answer

    def handleKeyAnswerGiven( self, ch ):
        # This is the enter key
        if( ch == ord('\n') or (self.review_mode == ReviewMode.ANKI and (ch == ord('1') or ch == ord('2') or ch == ord('3'))) ):
            self.nextReview()
            self.clearText()
            self.setAnswerBoxColorscheme( TerminalColorPalette.DEFAULT_HIGHLIGHT )
        elif( ch == ord('#') ):
            self.info_section_visible = True

    def handleKeyWaitingForDelay( self, ch ):
        if( time.time() - self.incorrect_start_time > self.DELAY_TIME ):
            if( ch == ord('\n') or (self.review_mode == ReviewMode.ANKI and (ch == ord('1') or ch == ord('2') or ch == ord('3'))) ):
                self.nextReview()
                self.clearText()
                self.setAnswerBoxColorscheme( TerminalColorPalette.DEFAULT_HIGHLIGHT )

    def answerReviewAnki( self, boolean ):
        result = self.rs.answerCurrentQuestionAnki( boolean )
        self.answerReviewCorrect() if result else self.answerReviewIncorrect()

    def answerReviewTyping( self, text ):
        result = self.rs.answerCurrentQuestionTyping( text )
        self.answerReviewCorrect() if result else self.answerReviewIncorrect()

    def answerReviewCorrect( self ):
        self.setState( ReviewState.ANSWER_GIVEN )
        if( self.lightning ):  # If lightning mode is enabled
            self.nextReview()
            self.clearText()
            return
        else:
            # Make answerbox show as correct style such as turning it green
            self.setAnswerBoxColorscheme( TerminalColorPalette.CORRECT_ANSWER_BOX )

    def answerReviewIncorrect( self ):
        # Set answebox show as incorrect style such as turning it red here
        self.setAnswerBoxColorscheme( TerminalColorPalette.INCORRECT_ANSWER_BOX )
        if( self.delay_on_incorrect ):
            # Starts the delay
            self.setState( ReviewState.WAITING_FOR_INCORRECT_DELAY )
            self.incorrect_start_time = time.time()
        else:
            self.setState( ReviewState.ANSWER_GIVEN )

    def nextReview( self ):
        self.rs.getNextReview()
        self.setState( ReviewState.READY_FOR_ANSWER )
        self.info_section_visible = False

    def showAnswer( self ):
        self.text = ", ".join( self.rs.getCorrectAnswer() )
        self.setState( ReviewState.ANSWER_SHOWN )

    def drawSubjectType( self ):
        try:
            subject_type = self.rs.current_review_item.subject.object
            x = self.getRelativeCenterX( subject_type )
            y = self.getAbsoluteCenterY() - 4
            self.scr.attron(curses.A_BOLD)
            if( subject_type == "vocabulary" ):
                self.scr.addstr( y, x, subject_type, curses.color_pair(TerminalColorPalette.REVIEW_VOCABULARY) )
            elif( subject_type == "kanji" ):
                self.scr.addstr( y, x, subject_type, curses.color_pair(TerminalColorPalette.REVIEW_KANJI) )

            self.scr.attroff(curses.A_BOLD)

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawKanji.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawKanji.', exc_info=True )
            curses.endwin()
            print( e )

    def drawKanji( self ):
        try:
            " Will need to add check here to see if characters is none and will need to ignore radicals that only have pics"
            " A more far-fetched idea may use ascii text to create a representation of the image of the radical"
            kanji = self.rs.current_review_item.subject.characters
            kanji_x = self.getRelativeCenterX( kanji ) - 1
            kanji_y = self.getAbsoluteCenterY() - 2

            # Add kanji text to screen
            self.scr.addstr( kanji_y, kanji_x, kanji )

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawKanji.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawKanji.', exc_info=True )
            curses.endwin()
            print( e )

    def drawTopStatsBar( self ):
        try:
            total_reviews_left = self.rs.getTotalReviewsRemaining()
            total_done_reviews = self.rs.total_done_reviews
            percent_correct = self.rs.getPercentCorrectReviews()

            top_stats_bar_str = "To Do: {} -- Done: {} -- Pct: {:>5.2f}".format( total_reviews_left, total_done_reviews, percent_correct )

            # 
            start_x = int( self.width - len( top_stats_bar_str ) - 1 )
            # We start the list at the top
            start_y = int( 0 )

            # 
            self.scr.addstr( start_y, start_x, top_stats_bar_str )

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawTopStatsBar.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawTopStatsBar.', exc_info=True )
            curses.endwin()
            print( e )

    def drawStatusBar( self, message="" ):
        try:
            # Set statusbar string, append message, and slice to width to prevent wrapping
            statusbarstr = "| {} | change mode(`) | ignore answer(!) | exit(~) | {}".format( self.review_mode, message )[:self.width]

            # Render status bar
            self.scr.attron(curses.color_pair( TerminalColorPalette.DEFAULT_HIGHLIGHT ))
            self.scr.addstr(self.height-1, 0, statusbarstr)
            self.scr.addstr(self.height-1, len(statusbarstr), " " * (self.width - len(statusbarstr) - len(message) - 1))
            self.scr.attroff(curses.color_pair(3))

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawStatusBar.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawStatusBar.', exc_info=True )
            curses.endwin()
            print( e )

    def drawQuestionType( self ):
        try:
            question_type = self.rs.current_question
            y = self.getAbsoluteCenterY()
            x = self.getRelativeCenterX( question_type )
            self.scr.attron(curses.A_BOLD)
            if( question_type == "meaning" ):
                self.scr.addstr( y, x, question_type, curses.color_pair( TerminalColorPalette.MEANING_QUESTION ) )
            elif( question_type == "reading" ):
                self.scr.addstr( y, x, question_type, curses.color_pair( TerminalColorPalette.READING_QUESTION ) )

            self.scr.attroff(curses.A_BOLD)

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawQuestionType.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawQuestionType.', exc_info=True )
            curses.endwin()
            print( e )

    def drawAnswerBox( self, text ):
        try:
            if( len(text) >= self.width ):
                text = text[:self.width]
                answer_box_str = text
            else:
                spacing_len = int( (self.width//2) - (len( text )//2) - (len(text)%2) )
                spacing = " " * spacing_len
                answer_box_str = "{}{}{}".format( spacing, text, spacing )
                while( len( answer_box_str ) < self.width - 1):
                    answer_box_str += " "

            y = self.getAbsoluteCenterY() + 1
            x = 0
            color_mode = self.getAnswerBoxColorscheme()
            self.scr.addstr( y, x, answer_box_str, curses.color_pair( color_mode ) )

        except KeyboardInterrupt:
            self.log.exception( 'Keyboard interrupt occured during drawAnswerBox.', exc_info=True )
            return

        except Exception as e:
            self.log.exception( 'Exception occured during drawAnswerBox.', exc_info=True )
            curses.endwin()
            print( e )

    def setAnswerBoxColorscheme( self, colorscheme ):
        self.answer_box_colorscheme = colorscheme

    def getAnswerBoxColorscheme( self ):
        return( self.answer_box_colorscheme )

    def drawReviewInfoSection( self ):
        q = self.rs.current_question
        s = self.rs.current_review_item.subject_type
        if( s == "radical" ):
            self.drawRadicalInfoScreen( q )
        elif( s == "kanji" ):
            self.drawKanjiInfoScreen( q )
        elif( s == "vocabulary" ):
            self.drawVocabularyInfoScreen( q )

    def drawRadicalInfoScreen( self, q ):
        x_zero = 0
        x_width = self.width
        y = self.getAbsoluteCenterY() + 2
        if( q == "meaning" ):
            self.scr.addstr( y, x_zero, "Meanings: {}".format( self.rs.current_review_item.subject.getMeaningsString() ) ) # Meaning
            self.scr.addstr( y+1, x_zero, "User Synonyms" ) # User Synonyms
            self.scr.addstr( y+2, x_zero, self.rs.current_review_item.subject.amalgamation_subject_ids ) # Radical Components
            # self.scr.addstr( y, x_width, self.rs.current_review_item.subject.meaning_mnemonic ) # Meaning Mnemonic
            # self.scr.addstr( y+1, x_width, self.rs.current_review_item.subject.meaning_hint ) # Meaning Hint
            # self.scr.addstr( y+2, x_width, "Meaning Note" ) # Meaning Note

    def drawKanjiInfoScreen( self, q ):
        x_zero = 0
        x_width = self.width
        y = self.getAbsoluteCenterY() + 2
        if( q == "meaning" ):
            self.scr.addstr( y, x_zero, "Meanings: {}".format( self.rs.current_review_item.subject.getMeaningsString() ) ) # Meaning
            self.scr.addstr( y+1, x_zero, "User Synonyms" ) # User Synonyms
            self.scr.addstr( y+2, x_zero, str( self.rs.current_review_item.subject.amalgamation_subject_ids ) ) # Radical Components
            # self.scr.addstr( y, x_width, self.rs.current_review_item.subject.meaning_mnemonic ) # Meaning Mnemonic
            # self.scr.addstr( y+1, x_width, self.rs.current_review_item.subject.meaning_hint ) # Meaning Hint
            # self.scr.addstr( y+2, x_width, "Meaning Note" ) # Meaning Note

        elif( q == "reading" ):
            self.scr.addstr( y, x_zero, "Readings: {}".format( self.rs.current_review_item.subject.getReadingsString() ) ) # Reading
            self.scr.addstr( y+1, x_zero, str( self.rs.current_review_item.subject.amalgamation_subject_ids ) ) # Radical Components
            # self.scr.addstr( y, x_width, self.rs.current_review_item.subject.reading_mnemonic ) # Reading Mnemonic
            # self.scr.addstr( y+1, x_width, self.rs.current_review_item.subject.reading_hint ) # Reading Hint
            # self.scr.addstr( y+2, x_width, "Reading Note" ) # Meaning Note

    def drawVocabularyInfoScreen( self, q ):
        x_zero = 0
        x_width = self.width
        y = self.getAbsoluteCenterY() + 2
        if( q == "meaning" ):
            self.scr.addstr( y, x_zero, "Meanings: {}".format( self.rs.current_review_item.subject.getMeaningsString() ), curses.color_pair(1) ) # Meaning
            self.scr.addstr( y+1, x_zero, "User Synonyms", curses.color_pair(1) ) # User Synonyms
            self.scr.addstr( y+2, x_zero, "Part of Speech: {}".format( self.rs.current_review_item.subject.getPartsOfSpeechString() ), curses.color_pair(1) ) # Parts of speech
            # self.scr.addstr( y, x_width, self.rs.current_review_item.subject.component_subject_ids ) # Component Subject IDs
            # self.scr.addstr( y+1, x_width, self.rs.current_review_item.subject.meaning_mnemonic ) # Meaning Mnemonic
            # self.scr.addstr( y+2, x_width, "Meaning Note" ) # Meaning Note

        elif( q == "reading" ):
            self.scr.addstr( y, x_zero, "Readings: {}".format( self.rs.current_review_item.subject.getReadingsString() ) ) # Reading
            self.scr.addstr( y+1, x_zero, "Part of Speech: {}".format( self.rs.current_review_item.subject.getPartsOfSpeechString() ) ) # Parts of speech
            # self.scr.addstr( y, x_width, self.rs.current_review_item.subject.component_subject_ids ) # Component Subject IDs
            # self.scr.addstr( y+1, x_width, self.rs.current_review_item.subject.reading_mnemonic ) # Meaning Mnemonic
            # self.scr.addstr( y+2, x_width, "Reading Note" ) # Meaning Note

    def getAbsoluteCenterY( self ):
        return( self.height//2 )

    def getRelativeCenterX( self, text ):
        return( (self.width//2) - (len( text )//2) - (len(text)%2) )

    def __del__(self):
        curses.nocbreak()
        self.scr.keypad(False)
        curses.echo()
        curses.endwin()


def main():
    wktui = WKTUI()
    wktui.drawReviewScreen()

if __name__ == "__main__":
    main()
