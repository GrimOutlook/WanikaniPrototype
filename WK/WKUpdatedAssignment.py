from settings import Settings
from WKObject import WKObject

class WKUpdatedAssignment( WKObject ):
    def __init__( self, data, wk_db, settings=None ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        self.settings = Settings() if settings == None else settings
        self.log = self.settings.logging

        WKObject.__init__( self, data, wk_db )
        self.subject_id             = data["subject_id"]
        self.started_datetime       = data["started_datetime"]

    def insertIntoDatabase( self ):
        if( self.settings.settings["debug"]["log_database_update_insertion"] ):
            self.log.debug("Inserting updated assignment of subject id: {} into database".format(self.subject_id))

        sql = """ INSERT OR REPLACE INTO updated_assignment(
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
