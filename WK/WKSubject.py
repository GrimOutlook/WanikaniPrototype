from WKObject import WKObject
import ast # This is for converting the returned database info into dictonaries easier

class WKSubject( WKObject ):
    def __init__( self, data, wk_db ):
        WKObject.__init__( self, data, wk_db )
        self.api_url                = data["api_url"]
        self.last_updated_datetime  = data["last_updated_datetime"]
        self.created_datetime       = data["created_datetime"]
        self.document_url           = data["document_url"]
        self.hidden_datetime        = data["hidden_datetime"]
        self.lesson_position        = data["lesson_position"]
        self.level                  = data["level"]
        self.auxiliary_meanings      = ast.literal_eval( data["auxiliary_meanings"] )
        self.characters             = data["characters"]
        self.meanings               = ast.literal_eval( data["meanings"] )
        self.slug                   = data["slug"]

        self.assignment = None
        self.subject = self

    def getAssignmentInfo( self ):
        if( self.assignment == None ):
            self.assignment = self.wk_db.getObjectBySubjectID( self.id, "assignment" )
            self.assignment.subject = self

        return( self )
