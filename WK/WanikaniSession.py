import requests, json, pprint, sys, pathlib, time, os
from random import shuffle # Used to shuffle reviews
from operator import itemgetter # Used for sorting lists of lists
from lxml import html

sys.path.append("./WK")
sys.path.append("./UI")
sys.path.append("..")

from settings import Settings
from WK import Pages
import WanikaniDatabase as WKDB
from WKSubject import WKSubject
from WKRadical import WKRadical
from WKKanji import WKKanji
from WKVocabulary import WKVocabulary
from WKDownloadItem import WKDownloadItem
from WKAssignment import WKAssignment
from WKUpdatedAssignment import WKUpdatedAssignment
from WKReview import WKReview
from WKUpdatedReview import WKUpdatedReview
from WKUser import WKUser

"""
By convention:
:r: is the response from either the API, a request in general, or a response from the Database
:d: is the data object inside a response that is returned from an API hit
"""

class WanikaniSession():
    BASE_API_URL = "https://api.wanikani.com/v2/"
    valid_collection_types = [ "subjects", "reviews", "assignments" ]

    def __init__( self, api_token="48768d92-fc9b-4616-9e4a-4fde5318daab", wk_db=None, settings=None ):
        self.settings = Settings() if settings == None else settings
        self.log = self.settings.logging

        # Initiallizes the main values necessary for querying to Wanikani API
        self.api_token = api_token
        self.header = {
            "Wanikani-Revision" : "20170710",
            "Authorization" : "Bearer " + self.api_token
        }

        self.wk_db = WKDB.WanikaniDatabase( settings=self.settings ) if wk_db == None else wk_db
        self.last_API_hit_time = 0

    def getFromAPI( self, url ):
        """
        There are two modes of retrieving the results.
        1) By directly accessing self.api_results after calling getFromAPI() or
        2) By assigning the value of the returned result of the function getFromAPI()
        """
        TIMEOUT = 5
        MAX_TRIES = 3
        tries = 1
        while( True ):
            # Does a get request to the Wanikani API and returns the results in dictionary form
            r = requests.get( url, headers=self.header, timeout=TIMEOUT )

            if( r.status_code == 200 ):
                self.api_results = r.json()
                return( self.api_results )

            elif( r.status_code == 429 ):
                # Sleeps for 20 seconds if error code is 429 because this code is displayed 
                # if you hit the rate limit
                time.sleep( 20 )

            else:
                if( tries >= MAX_TRIES  ):
                    self.log.debug( "Response error message:" )
                    self.log.debug( r.json() )
                    raise Exception("Server returning a status code other than 200. Status code is: {}".format(r.status_code))

                time.sleep(5)
                tries += 1

    def postToAPI( self, url, payload ):
        TIMEOUT = 5
        MAX_TRIES = 3
        tries = 1
        while( True ):
            # Does a post request to the Wanikani API and returns the results in dictionary form
            # The 'data' parameter is changed to 'json' so it automatically converts it to json
            # also it's the only way i've gotten it to work, converting it outside didn't work
            r = requests.post( url, headers=self.header, json=payload, timeout=TIMEOUT )

            if( r.status_code == 201 ):
                # Response code 201 means that the request was successful and a resource was created
                self.api_results = r.json()
                return( self.api_results )

            elif( r.status_code == 429 ):
                time.sleep( 20 )

            else:
                if( tries >= MAX_TRIES ):
                    self.log.debug( "Response error message:" )
                    self.log.debug( r.json() )
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
            item.downloadWKDataObject()
            item.removeFromTableByID( item, "download_queue" )

        self.wk_db.commitChanges()

    """
    #################################################################
    ################### Single insert functions #####################
    #################################################################
    """

    def importObjectIntoItemDatabase( self, r ):
        type_obj = r["object"]
        if( type_obj == "radical" ):
            obj = WKRadical.fromAPI( r, self.wk_db, settings=self.settings )
        elif( type_obj == "kanji" ):
            obj = WKKanji.fromAPI( r, self.wk_db, settings=self.settings )
        elif( type_obj == "vocabulary" ):
            obj = WKVocabulary.fromAPI( r, self.wk_db, settings=self.settings )
        elif( type_obj == "review" ):
            obj = WKReview.fromAPI( r, self.wk_db, settings=self.settings )
        elif( type_obj == "assignment" ):
            obj = WKAssignment.fromAPI( r, self.wk_db, settings=self.settings )
        elif( type_obj == "user" ):
            obj = WKUser.fromAPI( r, self.wk_db, settings=self.settings )
        else:
            raise Exception("Not a know object format. Object format is {}".format( type_obj ) )

        obj.insertIntoDatabase()

    def importSingleObjectIntoItemDatabase( self, r ):
        self.importObjectIntoItemDatabase( r )
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
                if( not self.wk_db.objectExistsInDatabase( obj["id"], obj["object"] ) ):
                    self.importObjectIntoItemDatabase( obj )

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
        self.importSingleObjectIntoItemDatabase( r )

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
