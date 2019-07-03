from WKDownloadItem import WKDownloadItem

class WKDownloadItem( WKObject ):
    def __init__( self, data, wk_db ):
        WKObject.__init__( self, data, wk_db )
        self.url = data["url"]
        self.filepath = data["filepath"]

    @classmethod
    def fromAPI( self, _id, obj, url, filepath, wk_db ):
        data = {
            "id"        : _id,
            "obj"       : obj,
            "url"       : url,
            "filepath"  : filepath
        }
        cls( data, wk_db )


    def insertIntoDatabase( self ):
        sql = """ INSERT INTO download_queue(
                id,
                object,
                url,
                filepath
        )

        VALUES( ?,?,?,? ) """

        download_item = (
            self.id,
            self.object,
            self.url,
            self.filepath
        )

        self.sql_exec( sql, download_item )
