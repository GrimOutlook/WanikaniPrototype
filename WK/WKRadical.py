from settings import Settings
from WKSubject import WKSubject
import ast # This is for converting the returned database info into dictonaries easier

class WKRadical( WKSubject ):
    # This constructor you use when pulling from database
    def __init__( self, data, wk_db, settings=None ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        self.settings = Settings() if settings == None else settings
        self.log = self.settings.logging

        WKSubject.__init__( self, data, wk_db  )
        self.character_images_info         = data["character_images_info"]
        self.character_images_path         = data["character_images_path"]
        self.amalgamation_subject_ids      = ast.literal_eval( data["amalgamation_subject_ids"] )

    # This constructor you use when pulling from the API
    # Takes response object dictionary rather than database dictionary
    @classmethod
    def fromAPI( cls, r, wk_db, settings=None ):
        d = r["data"]

        filepath = None

        data = {
            "id"                        : r["id"],
            "object"                    : r["object"],
            "api_url"                   : r["url"],
            "last_updated_datetime"     : r["data_updated_at"],
            "amalgamation_subject_ids"  : str( d["amalgamation_subject_ids"]),
            "auxiliary_meanings"        : str( d["auxiliary_meanings"]),
            "characters"                : d["characters"],
            "character_images_info"     : str( d["character_images"]),
            "character_images_path"     : filepath,
            "created_datetime"          : d["created_at"],
            "document_url"              : d["document_url"],
            "hidden_datetime"           : d["hidden_at"],
            "lesson_position"           : d["lesson_position"],
            "level"                     : d["level"],
            "meanings"                  : str( d["meanings"]),
            "meaning_mnemonic"          : d["meaning_mnemonic"],
            "slug"                      : d["slug"]
        }
        return( cls( data, wk_db, settings=settings ) )

    def insertIntoDatabase( self ):
        if( self.settings.settings["debug"]["log_database_insertion"] ):
            self.log.debug("Inserting radical of id {} into database".format(self.id))

        sql = """ INSERT OR REPLACE INTO radical(
                id,
                object,
                api_url,
                last_updated_datetime,
                amalgamation_subject_ids,
                auxiliary_meanings,
                characters,
                character_images_info,
                character_images_path,
                created_datetime,
                document_url,
                hidden_datetime,
                lesson_position,
                level,
                meanings,
                meaning_mnemonic,
                slug
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        radical = (
                self.id,
                self.object,
                self.api_url,
                self.last_updated_datetime,
                str( self.amalgamation_subject_ids ),
                str( self.auxiliary_meanings ),
                self.characters,
                str( self.character_images_info ),
                self.character_images_path,
                self.created_datetime,
                self.document_url,
                self.hidden_datetime,
                self.lesson_position,
                self.level,
                str( self.meanings ),
                self.meaning_mnemonic,
                self.slug
        )

        self.wk_db.sql_exec( sql, radical )

    def getDownloadable( self ):
        if( len( d["character_images"] ) > 0 ):
            pos, ext = self.getBestImagePosition( self.character_images_info )

            filepath = "./object/" + self.object + "/" + str(self.id) + "_image" + ext
        else:
            filepath = "None"

        dl = WKDownloadItem.fromAPI( self.id, "download_item", d["character_images"][pos]["url"], filepath )
        dl.insertIntoDatabase()

    @staticmethod
    def getBestImagePosition( c_i ):
        ranked = [ "without-css-original", "image/svg+xml", "\'original\'", "\'1024x1024\'" ]
        for item in ranked:
            pos = 0
            for image in c_i:
                if( item in str( image ) ):
                    break
                pos += 1

        WKDownloadItem.getExtension( c_i[ pos ] )

        return( pos, ext )

