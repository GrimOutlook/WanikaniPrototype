from WKObject import WKObject

class WKUpdatedAssignment( WKObject ):
    def __init__( self, data, wk_db ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        WKObject.__init__( self, data, wk_db )
        self.subject_id             = data["subject_id"]
        self.started_datetime       = data["started_datetime"]

    def insertIntoDatabase( self ):
        sql = """ INSERT INTO updated_assignment(
                id,
                object,
                subject_id,
                started_datetime
        )

        VALUES( ?,?,?,? ) """

        updated_assignment = (
            self.id,
            self.object,
            self.subject_id,
            self.started_datetime
        )

        self.wk_db.sql_exec( sql, updated_assignment )
