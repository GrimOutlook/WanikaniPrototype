import datetime

import WanikaniDatabase as WKDB
class WKObject():
    def __init__( self, data, wk_db ):
        self.id = data["id"]
        self.object = data["object"]
        self.wk_db = wk_db

    def insertIntoDatabase( self ):
        return

