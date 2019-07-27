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
        self.auxiliary_meanings     = ast.literal_eval( data["auxiliary_meanings"] )
        self.characters             = data["characters"]
        self.meanings               = ast.literal_eval( data["meanings"] )
        self.readings               = ast.literal_eval( data["readings"] ) if self.object != "radical" else []
        self.slug                   = data["slug"]

        self.assignment = None
        self.subject = self

    def getAssignmentInfo( self ):
        if( self.assignment == None ):
            self.assignment = self.wk_db.getObjectBySubjectID( self.id, "assignment" )
            self.assignment.subject = self
        return( self )

    def getPrimaryMeaning( self ):
        return( [ meaning["meaning"] for meaning in self.meanings if meaning["primary"] == True ] )

    def getPrimaryReading( self ):
        return( [ reading["reading"] for reading in self.readings if reading["primary"] == True ] )

    def getMeaningsString( self ):
        meanings = [ x["meaning"] for x in self.meanings if x["accepted_answer"] == True ]
        string = ", ".join( meanings )
        return( string )

    def getReadingsString( self ):
        readings = [ x["reading"] for x in self.readings if x["accepted_answer"] == True ]
        string = ", ".join( readings )
        return( string )