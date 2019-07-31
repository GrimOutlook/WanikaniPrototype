import datetime
from settings import Settings
from WKObject import WKObject
from WKUpdatedReview import WKUpdatedReview

class WKAssignment( WKObject ):
    def __init__( self, data, wk_db, settings=None ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        self.settings = Settings() if settings == None else settings
        self.log = self.settings.logging

        WKObject.__init__( self, data, wk_db )
        self.api_url                = data["api_url"]
        self.last_updated_datetime  = data["last_updated_datetime"]
        self.created_datetime       = data["created_datetime"]
        self.subject_id             = data["subject_id"]
        self.subject_type           = data["subject_type"]
        self.srs_stage              = data["srs_stage"]
        self.srs_stage_name         = data["srs_stage_name"]
        self.unlocked_datetime      = data["unlocked_datetime"]
        self.started_datetime       = data["started_datetime"]
        self.passed_datetime        = data["passed_datetime"]
        self.burned_datetime        = data["burned_datetime"]
        self.available_datetime     = data["available_datetime"]
        self.resurrected_datetime   = data["resurrected_datetime"]
        self.passed                 = data["passed"]
        self.resurrected            = data["resurrected"]
        self.hidden                 = data["hidden"]
        self.done                   = data["done"]

        self.last_review = None
        self.current_review = None
        self.assignment = self
        self.subject = None

    @classmethod
    def fromAPI( cls, r, wk_db, settings=None ):
        d = r["data"]
        data = {
            "id"                    : r["id"],
            "object"                : r["object"],
            "api_url"               : r["url"],
            "last_updated_datetime" : r["data_updated_at"],
            "created_datetime"      : d["created_at"],
            "subject_id"            : d["subject_id"],
            "subject_type"          : d["subject_type"],
            "srs_stage"             : d["srs_stage"],
            "srs_stage_name"        : d["srs_stage_name"],
            "unlocked_datetime"     : d["unlocked_at"],
            "started_datetime"      : d["started_at"],
            "passed_datetime"       : d["passed_at"],
            "burned_datetime"       : d["burned_at"],
            "available_datetime"    : d["available_at"],
            "resurrected_datetime"  : d["resurrected_at"],
            "passed"                : str( d["passed"]),
            "resurrected"           : str( d["resurrected"]),
            "hidden"                : str( d["hidden"]),
            "done"                  : False
        }
        return( cls( data, wk_db, settings=settings ) )

    def getSubject( self ):
        # Sets subject attribute to subject and returns subject just in case thats more convenient
        self.subject = self.wk_db.getObjectBySubjectID( self.subject_id, self.subject_type )
        self.subject.assignment = self

        return( self )

    def getNewReview( self ):
        self.current_review = WKUpdatedReview.fromAssignment( self.id, self.object, self.subject_id, self.wk_db )
        return( self )

    def isAvailableNow( self ):
        return( self.available_datetime != None and not self.done and
               datetime.datetime.fromisoformat( self.available_datetime.strip("Z") ) < datetime.datetime.now() )

    def insertIntoDatabase( self ):
        if( self.settings.settings["debug"]["log_database_insertion"] ):
            self.log.debug( "Inserting assignment with subject id: {} into database".format( self.subject_id ) )

        sql = """ INSERT OR REPLACE INTO assignment(
                id,
                object,
                api_url,
                last_updated_datetime,
                created_datetime,
                subject_id,
                subject_type,
                srs_stage,
                srs_stage_name,
                unlocked_datetime,
                started_datetime,
                passed_datetime,
                burned_datetime,
                available_datetime,
                resurrected_datetime,
                passed,
                resurrected,
                hidden,
                done
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        assignment = (
                self.id,
                self.object,
                self.api_url,
                self.last_updated_datetime,
                self.created_datetime,
                self.subject_id,
                self.subject_type,
                self.srs_stage,
                self.srs_stage_name,
                self.unlocked_datetime,
                self.started_datetime,
                self.passed_datetime,
                self.burned_datetime,
                self.available_datetime,
                self.resurrected_datetime,
                str( self.passed ),
                str( self.resurrected ),
                str( self.hidden ),
                self.done
        )

        self.wk_db.sql_exec( sql, assignment )

    def updateDone( self, done ):
        self.done = done
        sql = "UPDATE assignment SET done={} WHERE subject_id={}".format( done, self.subject_id )
        self.wk_db.sql_exec( sql )
        self.wk_db.commitChanges()

    def removeFromDatabase( self ):
        sql = "DELETE FROM assignment WHERE subject_id=?"
        self.wk_db.sql_exec( sql, (self.subject_id,) )
        self.wk_db.commitChanges()
