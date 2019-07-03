from WKObject import WKObject

class WKAssignment( WKObject ):
    def __init__( self, data, wk_db ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        WKObject.__init__( self, data, wk_db )
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

        self.last_review = None
        self.current_review = None
        self.subject = None

    @classmethod
    def fromAPI( self, r, wk_db ):
        d = r["data"]
        data = {
            "id"                    : r["id"],
            "object"                : r["object"],
            "api_url"               : r["url"],
            "last_updated_datetime" : r["data_updated_at"],
            "created_at"            : d["created_at"],
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
            "hidden"                : str( d["hidden"])
        }
        cls( data, wk_db )

    def getSubject( self ):
        # Sets subject attribute to subject and returns subject just in case thats more convenient
        if( self.subject != None ):
            self.subject = self.wk_db.getObjectBySubjectID( self.id, self.object )
            self.subject.assignment = self

    def isAvailableNow( self ):
        return( self.available_datetime != None and
               datetime.datetime.fromisoformat( self.available_datetime.strip("Z") ) < datetime.datetime.now() )

    def insertIntoDatabase( self, wk_db ):
        sql = """ INSERT INTO assignment(
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
                hidden
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

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
                self.passed,
                self.resurrected,
                self.hidden
        )

        self.wk_db.sql_exec( sql, assignment )
