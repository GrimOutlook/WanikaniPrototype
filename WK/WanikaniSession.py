import requests, json, pprint, sys, pathlib, time, os
from random import shuffle # Used to shuffle reviews
from operator import itemgetter # Used for sorting lists of lists
from lxml import html

sys.path.append("./WK")
sys.path.append("..")

from settings import Settings
# from WK import WK
from WanikaniDatabase import WanikaniDatabase
#from ReviewSession import ReviewSession
#from LessonSession import LessonSession

"""
By convention:
:r: is the response from either the API, a request in general, or a response from the Database
:d: is the data object inside a response that is returned from an API hit
"""

class WanikaniSession():
    settings = Settings( "wanikani_session" )

    BASE_API_URL = "https://api.wanikani.com/v2/"
    valid_collection_types = [ "subjects", "reviews", "assignments" ]

    def __init__( self, api_token="48768d92-fc9b-4616-9e4a-4fde5318daab" ):
        # Initiallizes the main values necessary for querying to Wanikani API
        self.api_token = api_token
        self.header = {
            "Authorization" : "Bearer " + self.api_token
        }

        self.wk_db = WanikaniDatabase()
        self.last_API_hit_time = 0

    """
    The request code is a mess, will hopefully fix it at some point
    """
    def getFromAPI( self, url ):
        """
        There are two modes of retrieving the results.
        1) By directly accessing self.api_results after calling getFromAPI() or
        2) By assigning the value of the returned result of the function getFromAPI()
        """
        # Does a get request to the Wanikani API and returns the results in dictionary form
        r = requests.get( url, headers=self.header, timeout=11 )
        self.api_results = r.json()

        MAX_TRIES = 5
        tries = 1
        while( True ):
            if( r.status_code == 200 ):
                return( self.api_results )

            elif( r.status_code == 429 ):
                # Sleeps for 20 seconds if error code is 429 because this code is displayed 
                # if you hit the rate limit
                time.sleep( 20 )

            else:
                if( tries > MAX_TRIES  ):
                    raise Exception("Server returning a status code other than 200. Status code is: {}".format(r.status_code))

                time.sleep(5)
                tries += 1

    def postToAPI( self, url, payload ):
        # Does a get request to the Wanikani API and returns the results in dictionary form
        r = requests.post( url, headers=self.header, data=payload, timeout=11 )
        self.api_results = r.json()

        MAX_TRIES = 5
        tries = 1
        while( True ):
            if( r.status_code == 200 ):
                return( self.api_results )

            elif( r.status_code == 429 ):
                time.sleep( 20 )

            else:
                if( tries > MAX_TRIES ):
                    raise Exception("Server returning a status code other than 200. Status code is: {}".format(r.status_code))

                time.sleep(5)
                tries += 1


    def printAPIResults( self ):
        pprint.pprint( self.api_results )
        # pprint.pprint( self.api_results )

    # def updateAPIHitTime( self ):
        # self.last_API_hit_time = time.time()

    # def checkTimeSinceLastAPIHit():
        # return( time.time() - self.last_API_hit_time )

    def collectionIsOfValidType( self, collection_type ):
        return( collection_type in self.valid_collection_types )

    def downloadAllWKDataObjects( self, mode=None ):
        r = self.wk_db.getAllOfItemTypeFromTable( "download_queue" )
        for item in r:
            # Returned index 0 is ID, index 1 is url, and index 2 is filepath
            self.downloadWKDataObject( item.url, item.filepath, mode )
            item.removeFromTableByID( item, "download_queue" )

        self.wk_db.commitChanges()

    """
    ##############################################################
    ####################### Static methods #######################
    ##############################################################
    """

    @staticmethod
    def downloadWKDataObject( url, filepath, mode ):
        """
        :mode: can be "o" for overwrite.
        """
        if( mode != "o" and os.path.exists( filepath ) and os.path.getsize(filepath) > 0 ):
            return

        try:
            res = requests.get( url, timeout=10 )
        except requests.exceptions.ConnectTimeout:
            try:
                res = requests.get( url, timeout=10 )
            except requests.exceptions.ConnectTimeout:
                print( "Connection timed out. Stopping program..." )
                raise

        path = filepath.split("/")
        del(path[-1])
        path = "/".join(path)

        pathlib.Path( path ).mkdir( parents=True, exist_ok=True )

        with open( filepath, "wb" ) as f:
            for chunk in res.iter_content(1000):
                f.write( chunk )

    @staticmethod
    def getBestImagePosition( c_i ):
        ranked = [ "without-css-original", "image/svg+xml", "\'original\'", "\'1024x1024\'" ]
        for item in ranked:
            print(item)
            pos = 0
            for image in c_i:
                if( item in str( image ) ):
                    break
                pos += 1

        if( c_i[pos]["content_type"] == "image/png" ):
            extension = ".png"
        elif( c_i[pos]["content_type"] == "image/svg+xml" ):
            extension = ".svg"
        else:
            raise Exception("Image is not a known format. Format is: ".format(c_i[pos]["metadata"]["content_type"]))

        return( pos, extension )


    """
    #################################################################
    ################### Single insert functions #####################
    #################################################################
    """

    def importObjectIntoItemDatabase( self, r, mode ):
        type_obj = r["object"]
        if( type_obj == "radical" ):
            obj = WKRadical.fromAPI( r, wk_db )

        elif( type_obj == "kanji" ):
            obj =  WKKanji.fromAPI( r, wk_db )

        elif( type_obj == "vocabulary" ):
            obj =  WKVocabulary.fromAPI( r, wk_db )

        elif( type_obj == "review" ):
            obj =  WKReview.fromAPI( r, wk_db )

        elif( type_obj == "assignment" ):
            obj =  WKAssignment.fromAPI( r, wk_db )

        elif( type_obj == "user" ):
            obj =  WKUser.fromAPI( r, wk_db )

        else:
            raise Exception("Not a know object format. Object format is {}".format( type_obj ) )

        obj.insertIntoDatabase()

        if( mode ==WK.SINGLE_MODE ):
            self.wk_db.commitChanges()

    """
    ##############################################################
    ################### Get object functions #####################
    ##############################################################
    """

    def querySubjectByID( self, item_id, item_type ):
        r = self.getFromAPI( self.BASE_API_URL + "subjects/" + str(item_id) ) # Full JSON results
        return( r )

    def getAllOfItemTypeFromTable( self, item_type ):
        return( self.wk_db.getAllOfItemTypeFromTable( item_type ) )

    """
    ###############################################################
    ################### Bulk insert functions #####################
    ###############################################################
    """
    def importAllFromCollectionIntoDatabase( self, collection_type ):
        if( not self.collectionIsOfValidType( collection_type ) ):
            raise Exception( "Invalid collection type. Collection is of type {}".format( collection_type ) )

        r = self.getFromAPI( self.BASE_API_URL + collection_type )

        while( True ): # Pseudo do-while loop
            d = r["data"]
            for obj in d:
                print( obj["id"] )
                if( not self.wk_db.objectExistsInDatabase( obj["id"], obj["object"] ) ):
                    self.importObjectIntoItemDatabase( obj, WK.BULK_MODE )

            next_url = r["pages"]["next_url"]
            self.wk_db.commitChanges()

            if( next_url == None ):
                break
            else:
                r = self.getFromAPI( next_url )

    def importAllCollectionsIntoDatabase( self ):
        for col in self.valid_collection_types:
            self.importAllFromCollectionIntoDatabase( col )

    def importUserIntoDatabase( self ):
        r = self.getFromAPI( self.BASE_API_URL + "user/" )
        self.importObjectIntoItemDatabase( r, WK.SINGLE_MODE )

    """
    ##############################################################
    ################### Post object functions ####################
    ##############################################################
    """
    def postAllUpdatedReviews( self ):
        updated_reviews = self.wk_db.getAllUpdatedReviews()
        for updated_review in updated_reviews:
            self.postUpdatedReview( updated_review )


    def postReview( self, updated_review ):
        # This posts reviews only

        # If review posting isn't allowed don't allow postin to take place
        if( not settings.settings["allow_review_posting"] ): return

        payload = { "review" : {
            "subject_id"                : updated_review["subject_id"],
            "incorrect_meaning_answers" : updated_review["incorrect_meaning_answers"],
            "incorrect_reading_answers" : updated_review["incorrect_reading_answers"],
            "created_at"                : updated_review["created_datetime"]
        }}

        r = requests.post( url, headers=self.header, data=payload, timeout=11 )
        # This should contain information pretaining to when the review will become available again
        # Will have to do a review myself to get a good generated response for parsing
        # The API has a pretty shoddy example
        self.api_results = r.json()

    def postAssignment( self ):
        # This posts lessons only
        pass
