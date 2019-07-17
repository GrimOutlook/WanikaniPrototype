import sys
sys.path.append("..")

from settings import Settings
from WanikaniDatabase import WanikaniDatabase
from WK import ReviewMode, Pages

from random import shuffle, randint, choice # For randomizing reviews
from difflib import SequenceMatcher # For checking for string similarity
from datetime import datetime # For timestamps
import re # For removing all non alpha-numeric-space characters from strings


class ReviewSession():
    def __init__( self ):
        # print("Initiallizing review session...")
        settings = Settings( Pages.REVIEW_SESSION )
        """
        :sort_mode: = how the reviews will be sorted
        :amount: = number of items in review queue at a time
        """
        self.sort_mode = settings.settings["review_session"]["sort_mode"]
        self.queue_size = settings.settings["review_session"]["queue_size"]
        self.wk_db = WanikaniDatabase()

        self.full_review_list = self.wk_db.getReviews()
        shuffle( self.full_review_list )

        self.current_review_queue = []
        self.setSortMode( self.sort_mode )

        self.current_review_index = 0
        self.current_review_item = self.current_review_queue[ self.current_review_index ]
        self.current_question = "meaning"

        """
        Statistics
        """
        self.initial_total_reviews = len( self.full_review_list ) + len( self.current_review_queue )
        self.total_correct_reviews = 0 # A review is deemed correct in this context if both the reading and meaning questions are answered with no incorrect responses
        self.total_done_reviews = 0
        self.total_questions_asked = 0
        self.total_correct_questions = 0

    def answerCurrentQuestion( self, answer, review_mode ):
        # print( "Answering current question..." )
        if( review_mode == ReviewMode.ANKI ):
            result = answer

        elif( review_mode == ReviewMode.TYPING ):
            result = False
            correct_answers = self.getCorrectAnswer()
            for correct_answer in correct_answers:
                # This just cheks that the answer is close enough to the correct value to be deemed correct
                if( self.answerIsCloseEnough( correct_answer, answer, self.current_question ) ):
                    result = True

        if( result ):
            # They answered correctly
            if( self.current_question == "meaning" ):
                self.current_review_item.current_review.meaning_answers_done = True
            elif( self.current_question == "reading" ):
                self.current_review_item.current_review.reading_answers_done = True

            # print( "Meaning answers done: {} -- Reading answers done: {}".format( self.current_review_item.current_review.meaning_answers_done, self.current_review_item.current_review.reading_answers_done ) )
            self.total_correct_questions += 1

        else:
            # They answer incorrectly
            if( self.current_question == "meaning" ):
                self.current_review_item.current_review.incorrect_meaning_answers += 1
            elif(self.current_question == "reading" ):
                self.current_review_item.current_review.incorrect_reading_answers += 1

        self.total_questions_asked += 1

        self.removeDoneItems()
        self.pickNextItem()
        self.getQuestion()

        return( result )

    def getQuestion( self ):
        # print("Getting next question...")
        if( self.current_review_item.current_review.meaning_answers_done ):
            self.current_question = "reading"

        elif( self.current_review_item.current_review.reading_answers_done ):
            self.current_question = "meaning"

        else:
            self.current_question = choice( [ "reading", "meaning" ] )

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

            # Update statistics
            if( self.current_review_item.current_review.incorrect_meaning_answers == 0 and self.current_review_item.current_review.incorrect_reading_answers == 0 ):
                self.total_correct_reviews += 1

            self.total_done_reviews += 1

            # Removing the current item from the current review queue
            del( self.current_review_queue[ self.current_review_index ] )
            # For the number of items missing from current review queue
            for i in range( self.queue_size - len( self.current_review_queue ) ):
                # Add an item from the full review list to the current review queue
                self.current_review_queue.append( self.full_review_list[i] )
                # Removes the item from the full review list so it isn't chosen again
                del( self.full_review_list[i] )

        # print( self.current_review_queue )


    def pickNextItem( self ):
        # print("Picking next item...")
        # Picks a random number between 0 and the max queue size
        self.current_review_index = randint( 0, self.queue_size - 1 )
        # Gets the item stored at that index from the current review queue
        self.current_review_item = self.current_review_queue[ self.current_review_index ]
        # print( "Current characters: {}".format( self.current_review_item.subject.characters ) )

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

    def setSortMode( self, sort_mode ):
        """
        Scrap old queue and reparse sort mode. Re sort the total review list and form a new queue with any partially
        done reviews at the front

        Sort mode is passed in as a list of lists

        :sort_mode:
        Sort by SRS level
        Sort by Subject

        if "(("SRS","A"),("Subject","A"))" is passed in then you would get apprentince 1 reviews and inside of apprentice 1 it
        would be sorted by Level highest first and the inside level it would be sorted by radicals first then go on to kanji and vocabulary
        """
        # print( "Setting sort mode..." )

        if( sort_mode != None ):
            for i in range( len( self.current_review_queue ) ):
                self.full_review_list.append( self.full_review_list[i] )
                del( self.current_review_queue[i] )


            self.sort_mode.reverse() # reversing the sort mode means that it will be sorted in the correct order
            for item in self.sort_mode:
                if( item[0] == "SRS" ):
                    if( item[1] == "A" ):
                        self.full_review_list.sort( key=operator.attrgettr("srs_stage") )
                    else:
                        self.full_review_list.sort( key=operator.attrgettr("srs_stage"), reverse=True )

                elif( item[0] == "Subject" ):
                    if( item[1] == "A" ):
                        self.full_review_list = subjectSort( valid_reviews )
                    else:
                        self.full_review_list = subjectSort( valid_reviews, reverse=True )

        self.current_review_queue = [ self.full_review_list[i] for i in range( self.queue_size ) ]
        for i in range( self.queue_size ):
            del( self.full_review_list[i] )

    """
    #############################################################
    ################### Custom Sort functions ###################
    #############################################################
    """
    def subjectSort( l, reverse=False ):
        """
        :l: list for sorting
        :reverse: whether list should be sorted in reverse order
        """
        # print( "Sorting by subject..." )

        mapping = [
            [ "radical",    0 ],
            [ "kanji",      1 ],
            [ "vocabulary", 2 ]
        ]
        for item in l:
            for m in mapping:
                if( item.subject == m[0] ):
                    item.subject == m[1]

        sorted( l, key=operator.attrgetter("subject"), reverse=reverse )

        for item in l:
            for m in mapping:
                if( item.subject == m[1] ):
                    item.subject == m[0]

        return( l )

    """
    #############################################################
    ################### Getting functions #######################
    #############################################################
    """
    def getCorrectAnswer( self ):
        if( self.current_question == "meaning" ):
            question = self.current_review_item.subject.meanings
        elif( self.current_question == "reading" ):
            question = self.current_review_item.subject.readings

        correct_answers = []
        for answer in question:
            if( answer["accepted_answer"] ):
                correct_answers.append( answer[ self.current_question ] )

        return( correct_answers )

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
