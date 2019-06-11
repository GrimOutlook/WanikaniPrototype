from settings import Settings
from WanikaniDatabase import WanikaniDatabase

from random import shuffle, randint # For randomizing reviews
from difflib import SequenceMatcher # For checking for string similarity
from datetime import datetime # For timestamps
import re # For removing all non alpha-numeric-space characters from strings


class ReviewSession():
    def __init__( self, sort_mode=None, queue_size=10 ):
        settings = Settings( "review_session" )
        """
        :sort_mode: = how the reviews will be sorted
        :amount: = number of items in review queue at a time
        """
        self.sort_mode = sort_mode
        self.queue_size = queue_size
        self.wk_db = WanikaniDatabase()

        # Index 12 denotes the available at timestamp and must be less than the current timestamp to be a valid review
        # Index 12 can also be None if the item is burned so we must check for that since the strip method will throw an error
        self.full_review_list = self.wk_db.getReviews()
        shuffle( self.full_review_list )

        self.current_review_queue = []
        self.setSortMode( self.sort_mode )

        self.current_review_index = 0
        self.current_review_item = self.current_review_queue[ self.current_review_index ]
        self.current_question = "meaning"


    def answerCurrentQuestion( self, answer, review_mode ):
        """
        :review_mode: is either "a" for anki or "t" for typing
        """
        if( review_mode == "a" ):
            result = answer
        elif( review_mode == "t" ):
            result = False
            for meaning in self.current_review_item["meanings"]:
                if( meaning["accepted_answer"] and self.answerIsCloseEnough( meaning["meaning"], answer ) ):
                    result = True

        if( result ):
            # They answered correctly
            self.current_review_item[ self.current_question + "_answers_done"] == True
            self.current_review_item[ "completed_datetime" ] = datetime.now().isoformat(timespec="microseconds")

        else:
            # They answer incorrectly
            self.current_review_item["incorrect_" + self.current_question + "_answers"] += 1


        self.removeDoneItems()
        self.pickNextItem()

        return( result )

    def removeDoneItems( self ):
        """
        This function only checks current item since its the last updated and there is no need to check the others since they cant change
        without being the current item
        """
        if( self.current_review_item["meaning_answers_done"] and self.current_review_item["reading_answers_done"] ):
            # I need to make an updated_review entry and then remove the current item and add another in
            # Adding the updated review entry


            # Removing the current item and replacing it in the queue
            del( self.current_review_queue[ self.current_review_index ] )
            for i in range( self.queue_size - len( self.current_review_queue ) ):
                self.current_review_queue.append( self.full_review_list[i] )


    def pickNextItem( self ):
        self.current_review_index = randint( 0, self.queue_size - 1 )
        self.current_review_item = self.current_review_queue[ self.current_review_index ]

    def answerIsCloseEnough( self, key, answer ):
        re_key = re.sub('[^A-Za-z0-9 ]+', '', key.lower() )
        re_answer = re.sub('[^A-Za-z0-9 ]+', '', answer.lower() )
        return( SequenceMatcher(None, re_key, re_answer).ratio() > .70 )



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

        if( sort_mode != None ):
            for i in range( len( self.current_review_queue ) ):
                self.full_review_list.append( self.full_review_list[i] )
                del( self.current_review_queue[i] )


            self.sort_mode.reverse() # reversing the sort mode means that it will be sorted in the correct order
            for item in self.sort_mode:
                if( item[0] == "SRS" ):
                    if( item[1] == "A" ):
                        self.full_review_list.sort( key=itemgetter(6) )
                    else:
                        self.full_review_list.sort( key=itemgetter(6), reverse=True )


                elif( item[0] == "Subject" ):
                    if( item[1] == "A" ):
                        self.full_review_list = subjectSort( valid_reviews )
                    else:
                        self.full_review_list = subjectSort( valid_reviews, reverse=True )

        self.current_review_queue = [ self.full_review_list[i] for i in range( self.queue_size ) ]

    """
    #############################################################
    ################### Custom Sort functions ###################
    #############################################################
    """
    def subjectSort( l ,reverse=False ):
        """
        :l: list for sorting
        :reverse: whether list should be sorted in reverse order
        """
        mapping = [
            [ "radical",    0 ],
            [ "kanji",      1 ],
            [ "vocabulary", 2 ]
        ]
        for item in l:
            for m in mapping:
                if( item["subject"] == m[0] ):
                    item["subject"] == m[1]

        sorted( l, key=itemgetter("subject"), reverse=reverse )

        for item in l:
            for m in mapping:
                if( item["subject"] == m[1] ):
                    item["subject"] == m[0]

        return( l )