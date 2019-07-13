import json, os
from WK import Pages, ReviewMode

"""
I need to think about users with slower hard drives when I program this so no saving
every time a setting is changed and especially don't make it so the file must be read
every time a setting configuration is needed.
Honestly this may be a non issue since the program and especcialy the settings will be
rather small in size but I'd rather take it into consideration now rather than later.
"""

class Settings():
    def __init__( self, page ):

        self.BASE_PATH = self.getBasePath()
        settings_file = self.BASE_PATH + "/settings.json"
        with open( settings_file, "r" ) as f:
            self.settings = json.load( f )

        self.convert()

        # Settings for the settings module

        self.settings["general"]["BASE_PATH"] = self.BASE_PATH

    def getSettings( self ):
        return( self.data[ self.page ] )

    def reverseParseData( self ):
        # This needs to be done before saving if saving the whole thing
        pass

    def saveSettings( self ):
        # print( json.dumps( self.data ) )

        if( self.settings["settings"]["allow_save_settings"] ):
            with open( settings_file, "w" ) as f:
                f.write( json.dumps( self.settings ) )

    def convert( self ):
        self.convertReviewMode()
        self.convertPages()

    def convertReviewMode( self ):
        review_mode = self.settings["review_page"]["review_mode"]
        if( review_mode == "anki" ):
            review_mode = ReviewMode.ANKI
        elif( review_mode == "typing" ):
            review_mode = ReviewMode.TYPING

        self.settings["review_page"]["review_mode"] = review_mode

    def convertPages( self ):
        page = self.settings["main_window"]["startup_page"]
        if( page == "review_page" ):
            page = Pages.REVIEW_PAGE
        elif( page == "home_page" ):
            page = Pages.HOME_PAGE

        self.settings["main_window"]["startup_page"] = page

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

