class ReviewSession():
    def __init__( sort_mode, queue_size, review_list ):
        """
        :sort_mode: = how the reviews will be sorted
        :amount: = number of items in review queue at a time
        """
        self.sort_mode = sort_mode
        self.queue_size = queue_size
        self.review_list = review_list

        self.current_review_queue = []
        self.current_review_item = None

    def changeQueueSize( self, queue_size ):
        """
        Resize the review queue while keeping the current order and expnading or shrinking as demanded
        """
        pass

    def changeSortMode( self, sort_mode ):
        """
        Scrap old queue and reparse sort mode. Re sort the total review list and form a new queue with any partially
        done reviews at the front
        """
        pass

    def startReview( self, sort_mode, amount_mode ):
        r = self.wk_db.getAllOfItemTypeFromTable( "assignment" )

        # Index 12 denotes the available at timestamp and must be less than the current timestamp to be a valid review
        # Index 12 can also be None if the item is burned so we must check for that since the strip method will throw an error
        valid_reviews = [ i for i in r if( i[12] != None and datetime.datetime.fromisoformat( i[12].strip("Z") ) < datetime.datetime.now() ) ]
        random.shuffle( valid_reviews )


        """
        Amount mode is simply an "s" or a "b" for single or bulk respectively
        bulk makes the queue the size of self.queue_size
        single makes the queue size 1

        Sort mode is passed in asa list of lists

        :sort_mode:
        Sort by SRS level
        Sort by Subject

        if "(("SRS","A"),("Subject","A"))" is passed in then you would get apprentince 1 reviews and inside of apprentice 1 it
        would be sorted by Level highest first and the inside level it would be sorted by radicals first then go on to kanji and vocabulary
        """
        sort_mode.reverse()
        for item in sort_mode:
            if( item[0] == "SRS" ):
                if( item[1] == "A" ):
                    valid_reviews.sort( key=itemgetter(6) )
                else:
                    valid_reviews.sort( key=itemgetter(6), reverse=True )

            elif( item[0] == "Subject" ):
                if( item[1] == "A" ):
                    valid_reviews = subjectSort( valid_reviews )
                else:
                    valid_reviews = subjectSort( valid_reviews, reverse=True )

        if( mode == "b" ):
            current_review_queue = [ valid_reviews[i] for i in range( self.queue_size ) ]
        elif( mode == "s" ):
            current_review_queue = valid_reviews[0]



    """
    #############################################################
    ###################Custom Sort functions ####################
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
                if( item[5] == m[0] ):
                    item[5] == m[1]

        sorted( l, key=itemgetter(5), reverse=reverse )

        for item in l:
            for m in mapping:
                if( item[5] == m[1] ):
                    item[5] == m[0]

        return( l )
