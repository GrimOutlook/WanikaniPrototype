from WKSubject import WKSubject
import ast # This is for converting the returned database info into dictonaries easier

class WKKanji( WKSubject ):
    def __init__( self, data, wk_db ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        WKSubject.__init__( self, data, wk_db  )
        self.amalgamation_subject_ids      = ast.literal_eval( data["amalgamation_subject_ids"] )
        self.component_subject_ids         = ast.literal_eval( data["component_subject_ids"] )
        self.meaning_hint                  = data["meaning_hint"]
        self.meaning_mnemonic              = data["meaning_mnemonic"]
        self.readings                      = ast.literal_eval( data["readings"] )
        self.reading_mnemonic              = data["reading_mnemonic"]
        self.reading_hint                  = data["reading_hint"]
        self.visually_similar_subject_ids  = ast.literal_eval( data["visually_similar_subject_ids"] )

    @classmethod
    def fromAPI( cls, r, wk_db ):
        d = r["data"]

        data = {
            "id"                            : r["id"],
            "object"                        : r["object"],
            "api_url"                       : r["url"],
            "last_updated_datetime"         : r["data_updated_at"],
            "amalgamation_subject_ids"      : str( d["amalgamation_subject_ids"]),
            "auxiliary_meanings"            : str( d["auxiliary_meanings"]),
            "characters"                    : d["characters"],
            "component_subject_ids"         : str( d["component_subject_ids"]),
            "created_datetime"              : d["created_at"],
            "document_url"                  : d["document_url"],
            "hidden_datetime"               : d["hidden_at"],
            "lesson_position"               : d["lesson_position"],
            "level"                         : d["level"],
            "meanings"                      : str( d["meanings"]),
            "meaning_hint"                  : d["meaning_hint"],
            "meaning_mnemonic"              : d["meaning_mnemonic"],
            "readings"                      : str( d["readings"]),
            "reading_mnemonic"              : d["reading_mnemonic"],
            "reading_hint"                  : d["reading_hint"],
            "slug"                          : d["slug"],
            "visually_similar_subject_ids"  : str( d["visually_similar_subject_ids"])
        }
        return( cls( data, wk_db ) )

    def insertIntoDatabase( self ):
        sql = """ INSERT INTO kanji(
                id,
                object,
                api_url,
                last_updated_datetime,
                amalgamation_subject_ids,
                auxiliary_meanings,
                characters,
                component_subject_ids,
                created_datetime,
                document_url,
                hidden_datetime,
                lesson_position,
                level,
                meanings,
                meaning_hint,
                meaning_mnemonic,
                readings,
                reading_mnemonic,
                reading_hint,
                slug,
                visually_similar_subject_ids
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        kanji = (
                self.id,
                self.object,
                self.api_url,
                self.last_updated_datetime,
                str( self.amalgamation_subject_ids ),
                str( self.auxiliary_meanings ),
                self.characters,
                str( self.component_subject_ids ),
                self.created_datetime,
                self.document_url,
                self.hidden_datetime,
                self.lesson_position,
                self.level,
                str( self.meanings ),
                self.meaning_hint,
                self.meaning_mnemonic,
                str( self.readings ),
                self.reading_mnemonic,
                self.reading_hint,
                self.slug,
                str( self.visually_similar_subject_ids )
        )

        self.wk_db.sql_exec( sql, kanji )
