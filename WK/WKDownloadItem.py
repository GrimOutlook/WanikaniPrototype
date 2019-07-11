import os
from WKObject import WKObject

class WKDownloadItem( WKObject ):
    def __init__( self, data, wk_db ):
        WKObject.__init__( self, data, wk_db )
        self.url = data["url"]
        self.filepath = data["filepath"]

    @classmethod
    def fromAPI( cls, _id, obj, url, filepath, wk_db ):
        data = {
            "id"        : _id,
            "obj"       : obj,
            "url"       : url,
            "filepath"  : filepath
        }
        return( cls( data, wk_db ) )


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

    # Needs to be converted to work with the new code, this is ripped from when using dictionaries
    def downloadWKDataObject():
        if( os.path.exists( self.filepath ) and os.path.getsize( self.filepath ) > 0 ):
            return

        try:
            res = requests.get( self.url, timeout=10 )
        except requests.exceptions.ConnectTimeout:
            try:
                res = requests.get( self.url, timeout=10 )
            except requests.exceptions.ConnectTimeout:
                print( "Connection timed out. Stopping program..." )
                raise

        path = self.filepath.split("/")
        del(path[-1])
        path = "/".join(path)

        pathlib.Path( path ).mkdir( parents=True, exist_ok=True )

        with open( self.filepath, "wb" ) as f:
            for chunk in res.iter_content(1000):
                f.write( chunk )

