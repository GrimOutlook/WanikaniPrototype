import sys
sys.path.append("..")

from settings import Settings
from WanikaniDatabase import WanikaniDatabase
from WK import ReviewMode, Pages, SRSStages, SortMode

from random import shuffle, randint, choice # For randomizing reviews
from difflib import SequenceMatcher # For checking for string similarity
from datetime import datetime # For timestamps
import re # For removing all non alpha-numeric-space characters from strings
import operator

class ReviewSession():
    def __init__( self ):
        # print("Initiallizing review session...")
        self.settings = Settings( Pages.REVIEW_SESSION )
        self.log = self.settings.logging

        self.log.debug( 'Review Session Started Initializing.' )
        """
        :sort_mode: = how the reviews will be sorted
        :amount: = number of items in review queue at a time
        """
        self.queue_size = self.settings.settings["review_session"]["queue_size"]
        self.wk_db = WanikaniDatabase()

        self.full_review_list = self.wk_db.getReviews()

        self.initSubjectCounts()
        self.initSRSCounts()
        self.initLevelCounts()

        # This section is for the ignore answer functionality
        self.previous_reviews = []          # List of previous reviews, will probably limit this in number, used for ignoring answers even after adding to database and continuing on to others
        self.previous_review_item = None    # This is simply the item that was used for answering the last question, not neccessarily different than the current review item
        self.previous_question = None       # Last question that was asked
        self.previous_result = None         # This is the result of the last answer the last question

        self.current_review_queue = []
        self.setSortMode( self.settings.settings["review_session"]["sort_mode"] )

        self.current_review_index = 0
        self.current_review_item = self.current_review_queue[ self.current_review_index ]
        self.getQuestion() # Sets current_question internally

        # Statistics stuff
        self.initial_total_reviews = len( self.full_review_list ) + len( self.current_review_queue )
        self.total_correct_reviews = 0  # A review is deemed correct in this context if both the reading and meaning questions are answered with no incorrect responses
        self.total_done_reviews = 0
        self.total_questions_asked = 0
        self.total_correct_questions = 0

        self.log.debug( 'Review Session Finished Initializing.' )

    def answerCurrentQuestionTyping( self, answer ):
        self.log.debug( "Answering current question in typing mode..." )
        result = False
        correct_answers = self.getCorrectAnswers()
        for correct_answer in correct_answers:
            # This just cheks that the answer is close enough to the correct value to be deemed correct
            if( self.answerIsCloseEnough( correct_answer, answer, self.current_question ) ):
                result = True

        self.answerCurrentQuestion( result )
        return( result )

    def answerCurrentQuestionAnki( self, boolean ):
        self.log.debug( "Answering current question in anki mode..." )
        self.answerCurrentQuestion( boolean )
        return( boolean )

    def answerCurrentQuestion( self, result ):
        self.previous_review_item = self.current_review_item
        self.previous_result = result
        self.previous_question = self.current_question

        if( result ):
            # They answered correctly
            if( self.current_question == "meaning" ):
                self.current_review_item.current_review.meaning_answers_done = True
            elif( self.current_question == "reading" ):
                self.current_review_item.current_review.reading_answers_done = True

            # print( "Meaning answers done: {} -- Reading answers done: {}".format(
            #         self.current_review_item.current_review.meaning_answers_done, self.current_review_item.current_review.reading_answers_done ) )
            self.total_correct_questions += 1

        else:
            # They answer incorrectly
            if( self.current_question == "meaning" ):
                self.current_review_item.current_review.incorrect_meaning_answers += 1
            elif(self.current_question == "reading" ):
                self.current_review_item.current_review.incorrect_reading_answers += 1

        self.total_questions_asked += 1

    def getNextReview( self ):
        self.log.debug("Getting next review...")
        self.removeDoneItems()
        self.pickNextItem()
        self.getQuestion()

    def getQuestion( self ):
        if( self.current_review_item.current_review.meaning_answers_done ):
            self.current_question = "reading"

        elif( self.current_review_item.current_review.reading_answers_done ):
            self.current_question = "meaning"

        else:
            self.current_question = choice( [ "reading", "meaning" ] )

        self.log.debug("New Question: {}".format( self.current_question ))

    def removeDoneItems( self ):
        """
        This function only checks current item since its the last updated and there is no need to check the others since they cant change
        without being the current item
        """
        if( self.current_review_item.current_review.meaning_answers_done and self.current_review_item.current_review.reading_answers_done ):
            # print( "Removing done item..." )
            # Set completed timestamp to now
            self.current_review_item.current_review.created_datetime = datetime.now().isoformat(timespec="microseconds")

            # Can be updated here to automatically upload the review to the api if so chosen
            # Add new review to database
            self.current_review_item.current_review.insertIntoDatabase()
            self.current_review_item.assignment.removeFromDatabase()

            # Update statistics
            if( self.current_review_item.current_review.incorrect_meaning_answers == 0 and self.current_review_item.current_review.incorrect_reading_answers == 0 ):
                self.total_correct_reviews += 1

            self.total_done_reviews += 1

            self.decreaseSubjectCount( self.current_review_item )
            self.decreaseSRSCount( self.current_review_item )
            self.decreaseLevelCount( self.current_review_item )

            # Moving the current item from the current review queue to the previous_reviews list
            self.previous_reviews.append( self.current_review_queue.pop( self.current_review_index ) )
            # For the number of items missing from current review queue
            for i in range( self.queue_size - len( self.current_review_queue ) ):
                # Move an item from the full review list to the current review queue
                self.current_review_queue.append( self.full_review_list.pop( 0 ) )
        # print( self.current_review_queue )

    def pickNextItem( self ):
        # print("Picking next item...")
        # Picks a random number between 0 and the max queue size
        self.current_review_index = randint( 0, self.queue_size - 1 )
        # Gets the item stored at that index from the current review queue
        self.current_review_item = self.current_review_queue[ self.current_review_index ]
        # print( "Current characters: {}".format( self.current_review_item.subject.characters ) )

    def resetLastAnswer( self ):
        # Checks if previous review item is none since that is the state it is in right as the program starts and we dont want
        # a nontype error
        if( self.previous_review_item == None  ):
            self.log.debug("Cannot ignore previous answer. No previous answer given")
            return

        self.log.debug( "Ignoring previous result='{}' for question='{}' for subject of id='{}'".format( self.previous_result, self.previous_question, self.previous_review_item.subject_id ) )
        if( self.previous_result ):
            # They answered correctly
            if( self.previous_question == "meaning" ):
                self.previous_review_item.current_review.meaning_answers_done = False
            elif( self.previous_question == "reading" ):
                self.previous_review_item.current_review.reading_answers_done = False

            # print( "Meaning answers done: {} -- Reading answers done: {}".format(
                    # self.previous_review_item.current_review.meaning_answers_done, self.previous_review_item.current_review.reading_answers_done ) )
            self.total_correct_questions -= 1

        else:
            # They answer incorrectly
            if( self.previous_question == "meaning" ):
                self.previous_review_item.current_review.incorrect_meaning_answers -= 1
            elif(self.previous_question == "reading" ):
                self.previous_review_item.current_review.incorrect_reading_answers -= 1

        self.total_questions_asked -= 1

        self.increaseSubjectCount( self.previous_review )
        self.increaseSRSCount( self.previous_review )
        self.increaseLevelCount( self.previous_review )

        # If the items aren't the same that means that the previous review has been moved from the current review queue
        # to the previous review list and must be put back to be reviewed again
        if( self.previous_review_item != self.current_review_item ):
            # Put item at front of the full item list
            self.full_review_list.insert( 0, self.previous_reviews[-1] )

    def increaseSubjectCount( self, item ):
        # Increases count of item subject type
        subject = item.subject_type
        self.subject_counts[subject] += 1

    def decreaseSubjectCount( self, item ):
        subject = item.subject_type
        self.subject_counts[subject] -= 1

    def increaseSRSCount( self, item ):
        # Increases count of item srs stage
        srs = item.srs_stage
        self.srs_counts[srs] += 1

    def decreaseSRSCount( self, item ):
        srs = item.srs_stage
        self.srs_counts[srs] -= 1

    def increaseLevelCount( self, item ):
        # Increases count of item level
        level = item.subject.level
        self.level_counts[level-1] += 1 # -1 since levels are 1 indexed

    def decreaseLevelCount( self, item ):
        level = item.subject.level
        self.level_counts[level-1] -= 1 # -1 since levels are 1 indexed

    @staticmethod
    def answerIsCloseEnough( key, answer, question ):
        # print("Checking if answer is close enough...")
        if( question == "meaning" ):
            re_key = re.sub('[^A-Za-z0-9 ]+', '', key.lower() )
            re_answer = re.sub('[^A-Za-z0-9 ]+', '', answer.lower() )
            return( SequenceMatcher(None, re_key, re_answer).ratio() > .70 )

        else:
            return( key == answer )

    """
    ###################################################################
    ################### Changing Settings functions ###################
    ###################################################################
    """

    def setQueueSize( self, queue_size ):
        """
        Resize the review queue while keeping the current order and expanding or shrinking as demanded
        Call this after sorting or else this is meaningless
        """
        # print( "Setting queue size..." )
        if( queue_size < self.queue_size ):
            # Simply slices queue down to new size
            cut_items = self.current_review_queue[ queue_size: ]
            for i in range( len( cut_items ) ):
                self.full_review_list.insert( i, cut_items[i] )

            self.current_review_queue = self.current_review_queue[ :queue_size ]

        elif( queue_size > self.queue_size ):
            for i in range( queue_size - self.queue_size ):
                self.current_review_queue.append( self.full_review_list[i] )
                del( self.full_review_list[i] )

    def setSortMode( self, sort_mode, reverse=False ):
        """
        Scrap old queue and reparse sort mode. Re sort the total review list and form a new queue with any partially
        done reviews at the front

        Sort mode is passed in as a list of lists

        :sort_mode:
        Sort by SRS level
        Sort by Subject

        if "[["SRS","A"],["Subject","A"]]" is passed in then you would get apprentince 1 reviews and inside of apprentice 1 it
        would be sorted by Level highest first and the inside level it would be sorted by radicals first then go on to kanji and vocabulary
        """
        # print( "Setting sort mode..." )

        if( sort_mode != None and ( not hasattr( self, "sort_mode" ) or sort_mode != self.sort_mode ) ): # Ensures that there is a a mode to sort with and that it is changing from the original sort

            self.sort_mode = sort_mode
            self.log.debug("Setting sort mode to {}".format(sort_mode))
            for i in range( len( self.current_review_queue ) ):
                self.full_review_list.append( self.current_review_queue.pop() )

            if( sort_mode == SortMode.RANDOM ):
                shuffle( self.full_review_list )
            elif( sort_mode == SortMode.LEVEL ):
                self.full_review_list = self.levelSort( self.full_review_list, reverse )
            elif( sort_mode == SortMode.SRS ):
                self.full_review_list = self.srsSort( self.full_review_list, reverse )
            elif( sort_mode == SortMode.SUBJECT ):
                self.full_review_list = self.subjectSort( self.full_review_list, reverse )

            self.current_review_queue = [ self.full_review_list.pop(0) for i in range( self.queue_size ) ]
            self.pickNextItem()

    """
    #############################################################
    ################### Custom Sort functions ###################
    #############################################################
    """
    def levelSort( self, l, reverse=False ):
        self.log.debug("Sorting reviews by level")
        sorted_l = sorted( l, key=lambda item: item.subject.level, reverse=reverse )
        return( sorted_l )

    def srsSort( self, l, reverse=False ):
        self.log.debug("Sorting reviews by srs")
        sorted_l = sorted( l, key=lambda item: item.srs_stage, reverse=reverse )
        return( sorted_l )

    def subjectSort( self, l, reverse=False ):
        """
        :l: list for sorting
        :reverse: whether list should be sorted in reverse order
        """
        self.log.debug("Sorting reviews by subject")

        mapping = [
            [ "radical",    0 ],
            [ "kanji",      1 ],
            [ "vocabulary", 2 ]
        ]
        # self.log.debug("Type: {}".format(type(self.full_review_list)))
        for item in l:
            for m in mapping:
                if( item.subject_type == m[0] ):
                    item.subject_type = m[1]

        sorted_l = sorted( l, key=lambda item: item.subject_type, reverse=reverse )

        for item in l:
            for m in mapping:
                if( item.subject_type == m[1] ):
                    item.subject_type = m[0]

        return( sorted_l )

    """
    #############################################################
    ################### Getting functions #######################
    #############################################################
    """
    def initSubjectCounts( self ):
        self.subject_counts = {
            "radical"   : 0,
            "kanji"     : 0,
            "vocabulary": 0
        }
        for item in self.full_review_list: self.subject_counts[item.subject_type] += 1

        self.log.debug( "Subject Makeup -- Radical: {}, Kanji: {}, Vocabulary: {}".format(
                        self.subject_counts["radical"], self.subject_counts["kanji"], self.subject_counts["vocabulary"] ) )

    def getSubjectCounts( self ):
        return( self.subject_counts )

    def getRadicalCount( self ):
        return( self.getSubjectCounts()["radical"] )

    def getKanjiCount( self ):
        return( self.getSubjectCounts()["kanji"] )

    def getVocabularyCount( self ):
        return( self.getSubjectCounts()["vocabulary"] )

    def initSRSCounts( self ):
        """
        Initializes SRS counts to a list where the index is the srs_stage and the list contents at an index
        is the number of items remaining, in a review session, at that srs stage
        """
        srs_c = [0] * 10 # 10 because there are 10 srs stages
        for i in range( len( self.full_review_list ) ):
            srs = self.full_review_list[i].srs_stage
            srs_c[ srs ] += 1

        self.log.debug( "SRS Makeup -- 0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}".format(
                        srs_c[0], srs_c[1], srs_c[2], srs_c[3], srs_c[4],
                        srs_c[5], srs_c[6], srs_c[7], srs_c[8], srs_c[9] ) )
        self.srs_counts = srs_c

    def getSRSCounts( self ):
        """
        Gets all srs stage counts and returns them as a list
        """
        return( self.srs_counts )

    def getSRSCount( self, srs ):
        """
        Gets count of items remaining in review session of certain srs stage
        """
        return( self.srs_counts[ srs ] )

    def initLevelCounts( self ):
        """
        Initializes a list of level counts where the index is the level and the contents at an index is the number of
        items remaining, during a review session, at that level
        """
        lvl_c = [0] * 60 # 60 because there are 60 levels. Must subtract 1 every time since the levels are 1 indexed but the list is 0 indexed
        for i in range( len( self.full_review_list ) ):
            lvl = self.full_review_list[i].subject.level
            lvl_c[ lvl - 1 ] += 1 # -1 since levels are 1 indexed

        s = "Level Makeup -- "
        for lvl in range( len( lvl_c ) ):
            s += "{}: {}, ".format( lvl+1, lvl_c[lvl] ) # +1 since wk levels are 1 indexed
        self.log.debug( s )
        self.level_counts = lvl_c

    def getLevelCounts( self ):
        """
        Returns all level counts
        """
        return( self.level_counts )

    def getLevelCount( self, level ):
        """
        Returns a count of number of items with a given level
        """
        return( self.level_counts[ level - 1 ] ) # -1 because levels are 1 indexed

    def getCorrectAnswers( self ):
        return( self.current_review_item.subject.getCorrectAnswers( self.current_question ) )

    def getPercentCorrectQuestions( self ):
        if( self.total_questions_asked == 0 ):
            return( 0 )
        else:
            return( ( self.total_correct_questions / self.total_questions_asked ) *100 )

    def getPercentCorrectReviews( self ):
        if( self.total_done_reviews == 0 ):
            return( 0 )
        else:
            return( ( self.total_correct_reviews / self.total_done_reviews ) *100 )

    def getTotalReviewsRemaining( self ):
        return( self.initial_total_reviews - self.total_done_reviews )
