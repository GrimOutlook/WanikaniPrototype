import json, os

"""
I need to think about users with slower hard drives when I program this so no saving
every time a setting is changed and especially don't make it so the file must be read
every time a setting configuration is needed
"""

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

        self.parseData()
        self.general["BASE_PATH"] = self.BASE_PATH

    def getSettings( self ):
        return( self.data[ self.page ] )

    def parseData( self ):
        self.general            = self.data["general"]
        self.main_window        = self.data["main_window"]
        self.wanikani_database  = self.data["wanikani_database"]
        self.wanikani_session   = self.data["wanikani_session"]
        self.review_session     = self.data["review_session"]
        self.home_page          = self.data["home_page"]
        self.review_page        = self.data["review_page"]
        # self.lesson_page        = self.data["lesson_page"]
        # self.settings_page      = self.data["settings_page"]
        self.settings_settings  = self.data[ "settings_module" ]

    def reverseParseData( self ):
        # This needs to be done before saving if saving the whole thing
        pass

    def saveSettings( self ):
        # print( json.dumps( self.data ) )

        self.all_settings[ self.page ] = self.settings # Do this to update the variable before writing

        if( self.settings_settings["allow_save_settings"] ):
            with open( settings_file, "w" ) as f:
                f.write( json.dumps( self.all_settings ) )

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

