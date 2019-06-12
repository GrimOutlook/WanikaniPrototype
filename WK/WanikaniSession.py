import requests, json, pprint, sys, pathlib, time, os
from random import shuffle # Used to shuffle reviews
from operator import itemgetter # Used for sorting lists of lists
from lxml import html

from settings import Settings
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

    def getFromAPI( self, url ):
        """
        There are two modes of retrieving the results.
        1) By directly accessing self.api_results after calling getFromAPI() or
        2) By assigning the value of the returned result of the function getFromAPI()
        """
        # Does a get request to the Wanikani API and returns the results in dictionary form
        r = requests.get( url, headers=self.header, timeout=11 )
        self.api_results = r.json()

        if( r.status_code == 200 ):
            return( self.api_results )

        else:
            time.sleep(5)
            r = requests.get( url, headers=self.header, timeout=11 )
            self.api_results = r.json()

            if( r.status_code == 200 ):
                return( self.api_results )

            else:
                raise Exception("Server returning a status code other than 200. Status code is: {}".format(r.status_code))

    def postToAPI( self, url, payload ):
        # Does a get request to the Wanikani API and returns the results in dictionary form
        r = requests.post( url, headers=self.header, timeout=11, data=payload )
        self.api_results = r.json()

        if( r.status_code == 200 ):
            return( self.api_results )

        else:
            time.sleep(5)
            r = requests.post( url, headers=self.header, timeout=11, data=payload )
            self.api_results = r.json()

            if( r.status_code == 200 ):
                return( self.api_results )

            else:
                raise Exception("Server returning a status code other than 200. Status code is: {}".format(r.status_code))

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
            self.downloadWKDataObject( item[1], item[2], mode )
            self.wk_db.removeFromTableByID( item[0], "download_queue" )

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
            d = r["data"]

            if( len( d["character_images"] ) > 0 ):
                pos, extension = self.getBestImagePosition( d["character_images"] )

                filepath = "./object/" + r["object"] + "/" + str(r["id"]) + "_image" + extension

                self.importItemIntoDownloadQueue( r["id"], d["character_images"][pos]["url"], filepath, mode  )

            else:
                filepath = "None"


            self.wk_db.createRadical((
                r["id"]                             ,
                r["url"]                            ,
                r["data_updated_at"]                ,
                str( d["amalgamation_subject_ids"] ),
                str( d["auxiliary_meanings"] )      ,
                d["characters"]                     ,
                str( d["character_images"] )        ,
                filepath                            ,
                d["created_at"]                     ,
                d["document_url"]                   ,
                d["hidden_at"]                      ,
                d["lesson_position"]                ,
                d["level"]                          ,
                str( d["meanings"] )                ,
                d["meaning_mnemonic"]               ,
                d["slug"]
            ))

        elif( type_obj == "kanji" ):
            d = r["data"]

            self.wk_db.createKanji((
                r["id"]                             ,
                r["url"]                            ,
                r["data_updated_at"]                ,
                str( d["amalgamation_subject_ids"] ),
                str( d["auxiliary_meanings"] )      ,
                d["characters"]                     ,
                str( d["component_subject_ids"] )   ,
                d["created_at"]                     ,
                d["document_url"]                   ,
                d["hidden_at"]                      ,
                d["lesson_position"]                ,
                d["level"]                          ,
                str( d["meanings"] )                ,
                d["meaning_hint"]                   ,
                d["meaning_mnemonic"]               ,
                str( d["readings"] )                ,
                d["reading_mnemonic"]               ,
                d["reading_hint"]                   ,
                d["slug"]                           ,
                str( d["visually_similar_subject_ids"] )
            ))

        elif( type_obj == "vocabulary" ):
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
                filepath = "./object/" + r["object"] + "/" + str(r["id"]) + "_audio" + extension
                self.importItemIntoDownloadQueue( r["id"], aud["url"], filepath, mode )


            else:
                print( "Item of id=" + str(r["id"]) + "has no audio files to be downloaded..." )
                filepath = "None"

            self.wk_db.createVocabulary((
                r["id"]                             ,
                r["url"]                            ,
                r["data_updated_at"]                ,
                str( d["auxiliary_meanings"] )      ,
                d["characters"]                     ,
                str( d["component_subject_ids"] )   ,
                str( d["context_sentences"] )       ,
                d["created_at"]                     ,
                d["document_url"]                   ,
                d["hidden_at"]                      ,
                d["lesson_position"]                ,
                d["level"]                          ,
                str( d["meanings"] )                ,
                d["meaning_mnemonic"]               ,
                str( d["parts_of_speech"] )         ,
                str( d["pronunciation_audios"] )    ,
                filepath                            ,
                str( d["readings"] )                ,
                d["reading_mnemonic"]               ,
                d["slug"]
            ))

        elif( type_obj == "review" ):
            d = r["data"]
            self.wk_db.createReview((
                r["id"]                         ,
                r["url"]                        ,
                r["data_updated_at"]            ,
                d["created_at"]                 ,
                d["assignment_id"]              ,
                d["subject_id"]                 ,
                d["starting_srs_stage"]         ,
                d["starting_srs_stage_name"]    ,
                d["ending_srs_stage"]           ,
                d["ending_srs_stage_name"]      ,
                d["incorrect_meaning_answers"]  ,
                d["incorrect_reading_answers"]
            ))

        elif( type_obj == "updated_review" ):
            self.wk_db.createUpdatedReview((
                r["id"]                         ,
                r["created_datetime"]           ,
                r["assignment_id"]              ,
                r["subject_id"]                 ,
                r["incorrect_meaning_answers"]  ,
                r["incorrect_reading_answers"]
            ))

        elif( type_obj == "assignment" ):
            d = r["data"]
            self.wk_db.createAssignment((
                r["id"]                         ,
                r["url"]                        ,
                r["data_updated_at"]            ,
                d["created_at"]                 ,
                d["subject_id"]                 ,
                d["subject_type"]               ,
                d["srs_stage"]                  ,
                d["srs_stage_name"]             ,
                d["unlocked_at"]                ,
                d["started_at"]                 ,
                d["passed_at"]                  ,
                d["burned_at"]                  ,
                d["available_at"]               ,
                d["resurrected_at"]             ,
                str( d["passed"] )              ,
                str( d["resurrected"] )         ,
                str( d["hidden"] )
            ))

        elif( type_obj == "updated_assignment" ):
            self.wk_db.createUpdatedAssignment((
                r["id"]                         ,
                d["subject_id"]                 ,
                d["started_datetime"]           ,
            ))

        else:
            raise Exception("Not a know object format. Object format is {}".format( type_obj ) )

        if( mode =="s" ):
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
                    self.importObjectIntoItemDatabase( obj, "b" )

            next_url = r["pages"]["next_url"]
            self.wk_db.commitChanges()

            if( next_url == None ):
                break
            else:
                r = self.getFromAPI( next_url )

    def importAllCollectionsIntoDatabase( self ):
        for col in self.valid_collection_types:
            self.importAllFromCollectionIntoDatabase( col )

    def importItemIntoDownloadQueue( self, item_id, url, filepath, mode ):
        self.wk_db.createDownloadQueueItem( item_id, url, filepath )
        if( mode == "s" ):
            self.wk_db.commitChanges()

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
