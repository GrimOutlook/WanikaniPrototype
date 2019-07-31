import ast
from settings import Settings
from WKSubject import WKSubject

class WKVocabulary( WKSubject ):
    def __init__( self, data, wk_db ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        self.settings = Settings()
        self.log = self.settings.logging

        WKSubject.__init__( self, data, wk_db  )
        self.component_subject_ids          = ast.literal_eval( data["component_subject_ids"] )
        self.context_sentences              = ast.literal_eval( data["context_sentences"] )
        self.parts_of_speech                = ast.literal_eval( data["parts_of_speech"] )
        self.pronunciation_audio_info       = data["pronunciation_audio_info"]
        self.pronunciation_audio_path       = data["pronunciation_audio_path"]
        self.meaning_mnemonic               = data["meaning_mnemonic"]
        self.reading_mnemonic               = data["reading_mnemonic"]

    @classmethod
    def fromAPI( cls, r, wk_db ):
        d = r["data"]   # This makes it easier to write in insert. Just data portion of JSON

        filepath = None

        data = {
            "id"                        : r["id"],
            "object"                    : r["object"],
            "api_url"                   : r["url"],
            "last_updated_datetime"     : r["data_updated_at"],
            "auxiliary_meanings"        : str( d["auxiliary_meanings"]),
            "characters"                : d["characters"],
            "component_subject_ids"     : str( d["component_subject_ids"]),
            "context_sentences"         : str( d["context_sentences"]),
            "created_datetime"          : d["created_at"],
            "document_url"              : d["document_url"],
            "hidden_datetime"           : d["hidden_at"],
            "lesson_position"           : d["lesson_position"],
            "level"                     : d["level"],
            "meanings"                  : str( d["meanings"]),
            "meaning_mnemonic"          : d["meaning_mnemonic"],
            "parts_of_speech"           : str( d["parts_of_speech"]),
            "pronunciation_audio_info"  : str( d["pronunciation_audios"]),
            "pronunciation_audio_path"  : filepath,
            "readings"                  : str( d["readings"]),
            "reading_mnemonic"          : d["reading_mnemonic"],
            "slug"                      : d["slug"]
        }
        return( cls( data, wk_db ) )

    def insertIntoDatabase( self ):
        if( self.settings.settings["debug"]["log_database_insertion"] ):
            self.log.debug("Inserting vocabulary of id: {} into database".format(self.id))

        sql = """ INSERT INTO vocabulary(
                id,
                object,
                api_url,
                last_updated_datetime,
                auxiliary_meanings,
                characters,
                component_subject_ids,
                context_sentences,
                created_datetime,
                document_url,
                hidden_datetime,
                lesson_position,
                level,
                meanings,
                meaning_mnemonic,
                parts_of_speech,
                pronunciation_audio_info,
                pronunciation_audio_path,
                readings,
                reading_mnemonic,
                slug
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        vocabulary = (
                self.id,
                self.object,
                self.api_url,
                self.last_updated_datetime,
                str( self.auxiliary_meanings ),
                self.characters,
                str( self.component_subject_ids ),
                str( self.context_sentences ),
                self.created_datetime,
                self.document_url,
                self.hidden_datetime,
                self.lesson_position,
                self.level,
                str( self.meanings ),
                self.meaning_mnemonic,
                str( self.parts_of_speech ),
                str( self.pronunciation_audio_info ),
                self.pronunciation_audio_path,
                str( self.readings ),
                self.reading_mnemonic,
                self.slug
        )

        self.wk_db.sql_exec( sql, vocabulary )

    def getDownloadable( self ):
        if( len( self.pronunciation_audio_info ) > 0 ):
            aud = self.pronunciation_audio_info[0]
            ext = WKDownloadItem.getExtension( aud["content_type"] )
            filepath = "./object/" + self.object + "/" + str(self.id) + "_audio" + ext
            dl = WKDownloadItem.fromAPI( self.id, "download_item", aud["url"], filepath )
            dl.insertIntoDatabase()

        else:
            print( "Item of id={} has no audio files to be downloaded...".format( str(self.id) ) )

    def getAllDownloadables( self ):
        for aud in self.pronunciation_audio_info:
            ext = WKDownloadItem.getExtension( aud["content_type"] )
            filepath = "./object/" + self.object + "/" + str(self.id) + "_audio" + ext
            dl = WKDownloadItem.fromAPI( self.id, "download_item", aud["url"], filepath )
            dl.insertIntoDatabase()

        if( len( self.pronunciation_audio_info ) <= 0 ):
            print( "Item of id={} has no audio files to be downloaded...".format( str(self.id) ) )

    def getPartsOfSpeechString( self ):
        return( ", ".join( self.parts_of_speech ) )
