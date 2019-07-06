import datetime
import ast # This is for converting the returned database info into dictonaries easier

import WanikaniDatabase as WKDB
class WKObject():
    def __init__( self, data, wk_db ):
        self.id = data["id"]
        self.object = data["object"]
        self.wk_db = wk_db

    def insertIntoDatabase( self ):
        return

