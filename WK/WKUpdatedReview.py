from WKObject import WKObject

class WKUpdatedReview( WKObject ):
    def __init__( self, data, wk_db ):
        WKObject.__init__( self, data, wk_db )
        self.created_datetime           = None
        self.assignment_id              = data["id"]
        self.subject_id                 = data["subject_id"]
        self.incorrect_meaning_answers  = 0
        self.incorrect_reading_answers  = 0
        self.meaning_answers_done       = False
        self.reading_answers_done       = False

    def insertIntoDatabase( self ):
        # This is all that is needed to post a review to wanikani
        sql = """ INSERT INTO updated_review(
                created_datetime,
                object,
                assignment_id,
                subject_id,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,?,? ) """

        updated_review = (
                self.created_datetime,
                self.object,
                self.subject_id,
                self.incorrect_meaning_answers,
                self.incorrect_reading_answers
        )

        self.wk_db.sql_exec( sql, updated_review )
