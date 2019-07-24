from settings import Settings
from WKObject import WKObject

class WKUpdatedReview( WKObject ):
    def __init__( self, data, wk_db ):
        self.settings = Settings()
        self.log = self.settings.logging

        self.object                     = data["object"]
        self.created_datetime           = None
        self.assignment_id              = data["assignment_id"]
        self.subject_id                 = data["subject_id"]
        self.incorrect_meaning_answers  = 0
        self.meaning_answers_done       = False
        if( self.object != "radical" ): # Radicals don't have readings
            self.incorrect_reading_answers  = 0
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

    def resetReview( self ):
        self.created_datetime           = None
        self.incorrect_meaning_answers  = 0
        self.incorrect_reading_answers  = 0
        self.meaning_answers_done       = False
        self.reading_answers_done       = False

    def reviveReview( self ):
        pass

    def insertIntoDatabase( self ):
        self.log.debug("Inserting updated review of subject id: {} into database".format(self.subject_id))
        # This is all that is needed to post a review to wanikani
        sql = """ INSERT INTO updated_review(
                assignment_id,
                created_datetime,
                object,
                subject_id,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,?,? ) """

        updated_review = (
                self.assignment_id,
                self.created_datetime,
                self.object,
                self.subject_id,
                self.incorrect_meaning_answers,
                self.incorrect_reading_answers
        )

        self.wk_db.sql_exec( sql, updated_review )

    def removeFromDatabase( self ):
        sql = "DELETE FROM updated_review WHERE subject_id=?"
        self.wk_db.sql_exec( sql, (self.subject_id,) )
