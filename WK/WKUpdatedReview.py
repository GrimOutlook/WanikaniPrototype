from WKObject import WKObject

class WKUpdatedReview( WKObject ):
    def __init__( self, data, wk_db ):
        self.object                     = data["object"]
        self.created_datetime           = None
        self.assignment_id              = data["assignment_id"]
        self.subject_id                 = data["subject_id"]
        self.incorrect_meaning_answers  = 0
        self.incorrect_reading_answers  = 0
        self.meaning_answers_done       = False
        self.reading_answers_done       = False

        self.wk_db = wk_db

    @classmethod
    def fromAssignment( cls, assignment_id, _object, subject_id, wk_db ):
        data = {
            "assignment_id" : assignment_id,
            "object"        : _object,
            "subject_id"    : subject_id,
            "incorrect_meaning_answers" : 0,
            "incorrect_reading_answers" : 0
        }
        return( cls( data, wk_db ) )

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
