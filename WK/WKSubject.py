from WKObject import WKObject
import ast # This is for converting the returned database info into dictonaries easier
import re

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
        self.component_subject_ids  = ast.literal_eval( data["component_subject_ids"] ) if self.object != "radical" else []
        self.characters             = data["characters"]
        self.meanings               = ast.literal_eval( data["meanings"] )
        self.readings               = ast.literal_eval( data["readings"] ) if self.object != "radical" else []
        self.meaning_mnemonic       = data["meaning_mnemonic"]
        self.reading_mnemonic       = data["reading_mnemonic"] if self.object != "radical" else ""
        self.slug                   = data["slug"]

        self.assignment = None
        self.subject = self

    def getAssignmentInfo( self ):
        if( self.assignment == None ):
            self.assignment = self.wk_db.getObjectBySubjectID( self.id, "assignment" )
            self.assignment.subject = self
        return( self )

    def getCorrectAnswers( self, question ):
        if( question == "meaning" ):
            answers = self.meanings
        elif( question == "reading" ):
            answers = self.readings

        correct_answers = []
        for answer in answers:
            if( answer["accepted_answer"] ):
                correct_answers.append( answer[ question ] )

        return( correct_answers )

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

    def getComponetSubjectsString( self ):
        chars = [ self.wk_db.getObjectBySubjectID( _id, "kanji" ).characters for _id in self.component_subject_ids ]
        return( ", ".join( chars ) )

    def getMeaningMnemonicString( self ):
        return( self.stripTags( self.meaning_mnemonic ) )

    def getReadingMnemonicString( self ):
        return( self.stripTags( self.reading_mnemonic ) )

    @staticmethod
    def stripTags( text ):
        return( re.sub( r"(<.*?>)", "", text ) )
