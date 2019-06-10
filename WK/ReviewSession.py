from WanikaniDatabase import WanikaniDatabase

from random import shuffle # For randomizing reviews if not sorting

class ReviewSession():
    def __init__( self, sort_mode=None, queue_size=10 ):
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
        print( len(self.full_review_list) )
        shuffle( self.full_review_list )

        self.current_review_queue = []
        self.setSortMode( self.sort_mode )

        self.current_review_item = self.current_review_queue[0]

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
