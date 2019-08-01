from settings import Settings
from datetime import datetime
from WKObject import WKObject
import WanikaniSession as WKSESS
import WKAssignment
import WKReview

class WKUpdatedReview( WKObject ):
    def __init__( self, data, wk_db, settings=None ):
        self.settings = Settings() if settings == None else settings
        self.log = self.settings.logging

        self.object                     = data["object"]
        self.created_datetime           = None
        self.assignment_id              = data["assignment_id"]
        self.subject_id                 = data["subject_id"]
        self.incorrect_meaning_answers  = 0
        self.meaning_answers_done       = False
        self.incorrect_reading_answers  = 0

        # Radicals don't have readings
        self.reading_answers_done = True if self.object == "radical" else False

        self.wk_db = wk_db

    @classmethod
    def fromAssignment( cls, assignment_id, _object, subject_id, wk_db, settings=None ):
        data = {
            "assignment_id" : assignment_id,
            "object"        : _object,
            "subject_id"    : subject_id,
            "incorrect_meaning_answers" : 0,
            "incorrect_reading_answers" : 0
        }
        return( cls( data, wk_db, settings=settings ) )

    def resetReview( self ):
        self.created_datetime           = None
        self.incorrect_meaning_answers  = 0
        self.incorrect_reading_answers  = 0
        self.meaning_answers_done       = False
        self.reading_answers_done       = False

    def reviveReview( self ):
        pass

    def setCreatedDatetime( self ):
        self.created_datetime = datetime.now().isoformat(timespec="microseconds") + "Z"

    def insertIntoDatabase( self ):
        if( self.settings.settings["debug"]["log_database_update_insertion"] ):
            self.log.debug("Inserting updated review of subject id: {} into database".format(self.subject_id))

        if( self.created_datetime == None ): self.setCreatedDatetime()

        # This is all that is needed to post a review to wanikani
        sql = """INSERT OR REPLACE INTO updated_review(
                assignment_id,
                object,
                created_datetime,
                subject_id,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,? ) """

        updated_review = (
                self.assignment_id,
                self.object,
                self.created_datetime,
                self.subject_id,
                self.incorrect_meaning_answers,
                self.incorrect_reading_answers
        )

        self.wk_db.sql_exec( sql, updated_review )

    def removeFromDatabase( self ):
        sql = "DELETE FROM updated_review WHERE subject_id=?"
        self.wk_db.sql_exec( sql, (self.subject_id,) )

    def upload( self, wk_sess=None ):
        wk_sess = WKSESS.WanikaniSession( wk_db=self.wk_db ) if wk_sess == None else wk_sess

        if( self.created_datetime == None ): self.setCreatedDatetime()

        payload = {
            "review" : {
                "subject_id" : self.subject_id,
                "incorrect_meaning_answers" : self.incorrect_meaning_answers,
                "incorrect_reading_answers" : self.incorrect_reading_answers,
                "created_at" : self.created_datetime
        } }
        self.log.debug( "Payload: {}".format( payload ) )

        url = wk_sess.BASE_API_URL + "reviews/"
        # self.log.debug("Posting review of subject_id={} to wanikani at url=\"{}\"...".format(self.subject_id, url))
        updated_info = wk_sess.postToAPI( url, payload )
        # self.log.debug( updated_info )
        review = WKReview.WKReview.fromAPI( updated_info, self.wk_db ).insertIntoDatabase()
        assignment = WKAssignment.WKAssignment.fromAPI( updated_info["resources_updated"]["assignment"], self.wk_db ).insertIntoDatabase()
        # Eventually I will also capture review statistics here
        # review_statistic = WKReviewStatistic.fromAPI( updated_info["resources_updated"]["review_statistic"] )

        # Remove self from database after being uploaded
        self.removeFromDatabase()
