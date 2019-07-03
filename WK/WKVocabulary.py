from WKSubject import WKSubject

class WKVocabulary( WKSubject ):
    def __init__( self, data, wk_db ):
        """
        The init function gets the parameters from a static list usually returned from an sql inquiry
        """
        WKSubject.__init__( self, data, wk_db  )
        self.component_subject_ids          = ast.literal_eval( data["component_subject_ids"] )
        self.parts_of_speech                = ast.literal_eval( data["parts_of_speech"] )
        self.pronunciation_audio_info       = data["pronunciation_audio_info"]
        self.pronunciation_audio_path       = data["pronunciation_audio_path"]
        self.meaning_mnemonic               = data["meaning_mnemonic"]
        self.readings                       = ast.literal_eval( data["readings"] )
        self.reading_mnemonic               = data["reading_mnemonic"]

    @classmethod
    def fromAPI( self, r, wk_db ):
        d = r["data"]   # This makes it easier to write in insert. Just data portion of JSON

        # It appears that some vocab may not have audio so i need to fix the out of range error
        # #4369 throws this error for example
        if( len( d["pronunciation_audios"] ) > 0 ):
            aud = d["pronunciation_audios"][0]
            if( aud["content_type"] == "audio/mpeg" ):
                extension = ".mpeg"
            elif( aud["content_type"] == "audio/ogg" ):
                extension = ".ogg"
            else:
                raise Exception("Audio is not a known format. Format is: ".format(aud["content_type"]))
            filepath = "./object/" + self.object + "/" + str(self.id) + "_audio" + extension

        else:
            print( "Item of id=" + str(self.id) + "has no audio files to be downloaded..." )
            filepath = "None"

        dl = WKDownloadItem.fromAPI( self.id, "download_item", aud["url"], filepath )
        dl.insertIntoDatabase()


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
        cls( data, wk_db )

    def insertIntoDatabase( self ):
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
                self.auxiliary_meanings,
                self.characters,
                self.component_subject_ids,
                self.context_sentences,
                self.created_datetime,
                self.document_url,
                self.hidden_datetime,
                self.lesson_position,
                self.level,
                self.meanings,
                self.meaning_mnemonic,
                self.parts_of_speech,
                self.pronunciation_audio_info,
                self.pronunciation_audio_path,
                self.readings,
                self.reading_mnemonic,
                self.slug
        )

        self.wk_db.sql_exec( sql, kanji )
