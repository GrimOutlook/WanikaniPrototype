from settings import Settings
from WKObject import WKObject

class WKReview( WKObject ):
    def __init__( self, data, wk_db ):
        self.settings = Settings()
        self.log = self.settings.logging

        WKObject.__init__( self, data, wk_db )
        self.api_url                    = data["api_url"]
        self.last_updated_datetime      = data["last_updated_datetime"]
        self.created_datetime           = data["created_datetime"]
        self.assignment_id              = data["id"]
        self.subject_id                 = data["subject_id"]
        self.starting_srs_stage         = data["starting_srs_stage"]
        self.starting_srs_stage_name    = data["starting_srs_stage_name"]
        self.ending_srs_stage           = data["ending_srs_stage"]
        self.ending_srs_stage_name      = data["ending_srs_stage_name"]
        self.incorrect_meaning_answers  = 0
        self.incorrect_reading_answers  = 0

    @classmethod
    def fromAPI( cls, r, wk_db ):
        d = r["data"]
        data = {
            "id"                        : r["id"],
            "object"                    : r["object"],
            "api_url"                   : r["url"],
            "last_updated_datetime"     : r["data_updated_at"],
            "created_datetime"          : d["created_at"],
            "assignment_id"             : d["assignment_id"],
            "subject_id"                : d["subject_id"],
            "starting_srs_stage"        : d["starting_srs_stage"],
            "starting_srs_stage_name"   : d["starting_srs_stage_name"],
            "ending_srs_stage"          : d["ending_srs_stage"],
            "ending_srs_stage_name"     : d["ending_srs_stage_name"],
            "incorrect_meaning_answers" : d["incorrect_meaning_answers"],
            "incorrect_reading_answers" : d["incorrect_reading_answers"]
        }
        return( cls( data, wk_db ) )

    def insertIntoDatabase( self ):
        if( self.settings.settings["debug"]["log_database_insertion"] ):
            self.log.debug("Inserting review of subject id: {} into database".format(self.subject_id))

        sql = """ INSERT OR REPLACE INTO review(
                id,
                object,
                api_url,
                last_updated_datetime,
                created_datetime,
                assignment_id,
                subject_id,
                starting_srs_stage,
                starting_srs_stage_name,
                ending_srs_stage,
                ending_srs_stage_name,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        review = (
                self.id,
                self.object,
                self.api_url,
                self.last_updated_datetime,
                self.created_datetime,
                self.assignment_id,
                self.subject_id,
                self.starting_srs_stage,
                self.starting_srs_stage_name,
                self.ending_srs_stage,
                self.ending_srs_stage_name,
                self.incorrect_meaning_answers,
                self.incorrect_reading_answers
        )
        self.wk_db.sql_exec( sql, review )
