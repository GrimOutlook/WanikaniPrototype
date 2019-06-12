import json, os

class Settings():
    def __init__( self, page ):

        self.BASE_PATH = self.getBasePath()
        settings_file = self.BASE_PATH + "/settings.json"
        with open( settings_file, "r" ) as f:
            self.data = json.load( f )

        self.page = page
        self.all_settings = self.data
        self.settings = self.data[ self.page ]

        # Settings for the settings module
        self.settings_settings = self.data[ "settings_module" ]

    def getSettings( self ):
        return( self.data[ self.page ] )

    # def parseData( self ):
        # self.review_page        = self.data["review_page"]
        # # self.lesson_page        = self.data["lesson_page"]
        # # self.wanikani_session   = self.data["wanikani_session"]
        # # self.wanikani_database  = self.data["wanikani_database"]
        # # self.home_page          = self.data["home_page"]

    def saveSettings( self ):
        print( json.dumps( self.data ) )

    @staticmethod
    def getBasePath():
        cwd = os.getcwd()
        cwd_split = cwd.split("/")
        found = None
        for i in range( len( cwd_split ) ):
            if( found == None and cwd_split[i] == "WanikaniPrototype" ):
                found = i

            elif( found != None ):
                del( cwd_split[i] )

        return( "/".join( cwd_split ) )

