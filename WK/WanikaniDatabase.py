import sqlite3
from sqlite3 import Error

import datetime # For calculating timestamps
import ast # This is for converting the returned database info into dictonaries easier
import sys
import os

sys.path.append("..")

from settings import Settings

from WK import Pages
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

class WanikaniDatabase():

    def __init__( self, database_filename=None ):
        self.settings = Settings( Pages.WANIKANI_DATABASE )

        """
        Items with multiple data points will be stored as text and be parsed as json for manipulation

        ##### For Radicals and Kanji #####

        ##### For Kanji and Vocabulary #####

        ##### List of items that will be stored as JSON #####
        :amalgamation_subject_ids:
        :auxilary_meanings:
        :meanings:
        :component_subject_ids
        :readings:
        :context_sentences:
        :parts_of_speech:
        :pronunciation_audios: ***May want to download it independently and then make a column for the path to it
        :visually_similar_ids:


        ##### For storing data #####
        I want to store only a single image or audio file per object. I will try and grab
        of the largest quality I can get. I will download the images or audio to a known directory and store the paths to each
        objects images or audio in the database rather than storing the data itself.

        ##### Timestamps #####
        Timestamps are stored in datetime.isoformat(timespec="microseconds") format
        Use datetime.datetime.fromisoformat( variable.strip("Z") ) to get the datetime data
        Possible optimization in storing timestap as posix timestamp but I will hold off for now

        ##### Object will always be the second argument for easier parsing
        """

        sql_create_table_radical = """CREATE TABLE IF NOT EXISTS radical (
                id integer PRIMARY KEY,
                object text,
                api_url text,
                last_updated_datetime text,
                amalgamation_subject_ids text,
                auxiliary_meanings text,
                characters text,
                character_images_info text,
                character_images_path text,
                created_datetime text,
                document_url text,
                hidden_datetime text,
                lesson_position integer,
                level integer,
                meanings text,
                meaning_mnemonic text,
                slug text
        );"""
        sql_create_table_kanji = """CREATE TABLE IF NOT EXISTS kanji (
                id integer PRIMARY KEY,
                object text,
                api_url text,
                last_updated_datetime text,
                amalgamation_subject_ids text,
                auxiliary_meanings text,
                characters text,
                component_subject_ids text,
                created_datetime text,
                document_url text,
                hidden_datetime text,
                lesson_position integer,
                level integer,
                meanings text,
                meaning_hint text,
                meaning_mnemonic text,
                readings text,
                reading_mnemonic text,
                reading_hint text,
                slug text,
                visually_similar_subject_ids text
        );"""
        sql_create_table_vocabulary = """CREATE TABLE IF NOT EXISTS vocabulary (
                id integer PRIMARY KEY,
                object text,
                api_url text,
                last_updated_datetime text,
                auxiliary_meanings text,
                characters text,
                component_subject_ids text,
                context_sentences text,
                created_datetime text,
                document_url text,
                hidden_datetime text,
                lesson_position integer,
                level integer,
                meanings text,
                meaning_mnemonic text,
                parts_of_speech text,
                pronunciation_audio_info text,
                pronunciation_audio_path text,
                readings text,
                reading_mnemonic text,
                slug text
        );"""
        sql_create_table_download_queue = """CREATE TABLE IF NOT EXISTS download_queue (
                id integer PRIMARY KEY,
                object text,
                url text,
                filepath text
        );"""
        sql_create_table_review = """CREATE TABLE IF NOT EXISTS review (
                id integer PRIMARY KEY,
                object text,
                api_url text,
                last_updated_datetime text,
                created_datetime text,
                assignment_id integer,
                subject_id integer,
                starting_srs_stage text,
                starting_srs_stage_name text,
                ending_srs_stage text,
                ending_srs_stage_name text,
                incorrect_meaning_answers integer,
                incorrect_reading_answers integer
        );"""
        sql_create_table_updated_review = """CREATE TABLE IF NOT EXISTS updated_review (
                assignment_id integer PRIMARY KEY,
                object text,
                created_datetime text,
                subject_id integer,
                incorrect_meaning_answers integer,
                incorrect_reading_answers integer
        );"""
        sql_create_table_assignment = """CREATE TABLE IF NOT EXISTS assignment (
                id integer PRIMARY KEY,
                object text,
                api_url integer,
                last_updated_datetime text,
                created_datetime text,
                subject_id integer,
                subject_type text,
                srs_stage integer,
                srs_stage_name text,
                unlocked_datetime text,
                started_datetime text,
                passed_datetime text,
                burned_datetime text,
                available_datetime text,
                resurrected_datetime text,
                passed text,
                resurrected text,
                hidden text
        );"""
        sql_create_table_updated_assignment = """CREATE TABLE IF NOT EXISTS updated_assignment (
                id integer PRIMARY KEY,
                object text,
                subject_id integer,
                started_datetime text
        );"""
        sql_create_table_user = """CREATE TABLE IF NOT EXISTS user(
                id text,
                object text,
                username text,
                level integer,
                max_level_granted_by_subscription integer,
                profile_url text,
                started_datetime text,
                subscribed text,
                current_vacation_started_datetime text,
                subscription text,
                preferences text
        );"""

        if( database_filename != None ):
            self.database_filename = database_filename
        else:
            self.database_filename = self.settings.BASE_PATH + "/wanikani.db"
        # path can equal either :memory: or a database file
        try:
            self.conn = sqlite3.connect( self.database_filename )
            self.conn.row_factory = sqlite3.Row
        except Error as e:
            print( e )
            self.conn.close()
            print("Connection to database failed. Closing...")
            exit()

        self.sql_exec( sql_create_table_radical )
        self.sql_exec( sql_create_table_kanji )
        self.sql_exec( sql_create_table_vocabulary )
        self.sql_exec( sql_create_table_download_queue )
        self.sql_exec( sql_create_table_review )
        self.sql_exec( sql_create_table_updated_review )
        self.sql_exec( sql_create_table_assignment )
        self.sql_exec( sql_create_table_updated_assignment )
        self.sql_exec( sql_create_table_user )

        self.commitChanges()

    def commitChanges( self ):
        self.conn.commit()

    def purgeDatabase( self ):
        if( self.database_filename != ":memory:" ):
            os.remove( self.database_filename )
        else:
            self.conn.close()
            self.conn.connect( self.database_filename )

    def sql_exec( self, sql, values=None ):
        if( self.conn != None ):
            c = self.conn.cursor()
        try:
            if( values != None ):
                c.execute( sql, values )
            else:
                c.execute( sql )

            return( c )

        except Error as e:
            print(e)
            print( "Executing sql command was unsuccessful..." )

    """
    ############################
    # Data gathering functions #
    ############################
    """
    def itemTypeIsValid( self, item_type ):
        valid_types = [ "radical", "kanji", "vocabulary", "review", "updated_review", "assignment", "updated_assignment", "download_queue", "user" ]
        return ( item_type in valid_types )

    def objectExistsInDatabase( self, item_id, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.sql_exec( "SELECT * FROM {} WHERE id=?".format(item_type), (item_id,) )
        return( len( c.fetchall() ) > 0 )

    def getUserCurrentLevel( self ):
        # The "0" index just means to select the first (and typically only) item
        level = self.getAllOfItemTypeFromTable( "user" )[0]["level"]
        return( level )

    def getSubjectObjectsOfGivenLevel( self, subject_type, level ):
        if( self.itemTypeIsValid( subject_type ) ):
            c = self.sql_exec( "SELECT * FROM {} WHERE level=?".format( subject_type ), (level,))
            return( self.parseDataList( c.fetchall() ) )

    def getAssignmentsBySRSStageName( self, level ):
        c = self.sql_exec( "SELECT * FROM assignment WHERE srs_stage_name=?", (level,))
        return( self.parseDataList( c.fetchall() ) )

    def getObjectByID( self, item_id, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.sql_exec( "SELECT * FROM {} WHERE id=?".format(item_type), (item_id,) )
        return( self.parseData( c.fetchone() ) )

    def getObjectBySubjectID( self, item_subject_id, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        item_id_prompt = {
            "radical"               : "id",
            "kanji"                 : "id",
            "vocabulary"            : "id",
            "review"                : "subject_id",
            "updated_review"        : "subject_id",
            "assignment"            : "subject_id",
            "updated_assignment"    : "subject_id"
        }

        c = self.sql_exec( "SELECT * FROM {0} WHERE {1}=?".format(item_type, item_id_prompt[ item_type ]), (item_subject_id,) )
        return( self.parseData( c.fetchone() ) )

    def getAllOfItemTypeFromTable( self, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.sql_exec( "SELECT * FROM {}".format(item_type ) )
        return( self.parseDataList( c.fetchall() ) )

    def removeFromTableByID( self, item_id, table ):
        if( not self.itemTypeIsValid( table ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.sql_exec( "DELETE FROM {} WHERE id=?".format( table ), (item_id,) )

    def parseData( self, data ):
        obj = data["object"]

        if( obj == "radical" ):
            new_obj = WKRadical( data, self )
        elif( obj == "kanji" ):
            new_obj = WKKanji( data, self )
        elif( obj == "vocabulary" ):
            new_obj = WKVocabulary( data, self )
        elif( obj == "download_item" ):
            new_obj = WKDownloadItem( data, self )
        elif( obj == "review" ):
            new_obj = WKReview( data, self )
        elif( obj == "updated_review" ):
            new_obj = WKUpdatedReview( data, self )
        elif( obj == "assignment" ):
            new_obj = WKAssignment( data, self )
        elif( obj == "updated_assignment" ):
            new_obj = WKUpdatedAssignment( data, self )
        elif( obj == "user" ):
            new_obj = WKUser( data, self )
        else:
            raise Exception( "Cannot parse object of unknown type. Object is of type {}".format(obj) )

        return( new_obj )


    def parseDataList( self, data_list ):
        # return( data_list )
        parsed_data = []
        for item in data_list:
            parsed_data.append( self.parseData( item ) )

        return( parsed_data )

    def getReviews( self ):
        """
        This function will return a dictonary element containing
        :subject_id: taken from assignments and subjects own table
        :subject: type such as "radical" taken from assignments
        :srs_stage_name: such as "Guru I" taken from assignments
        """
        reviews = []
        c = self.sql_exec("SELECT * FROM assignment")
        parsed_reviews = self.parseDataList( c.fetchall() )
        valid_reviews = [ item.getSubject().getNewReview() for item in parsed_reviews if item.isAvailableNow() ] # Gets items that are currently available and gets the coresponding subject object and creates a new review object as well

        return(valid_reviews)

    def getUpdatedReviews( self ):
        updated_reviews = []
        unparsed_updated_reviews = self.sql_exec("SELECT * from updated_review").fetchall()
        return( parseDataList( unparsed_updated_reviews ) )

    def getRecentlyUnlockedAssignments( self ):
        # Useful for populationg the recently unlocked list in the statistics area
        c = self.sql_exec(
            """ SELECT id,subject_type,subject_id,unlocked_datetime
                FROM assignment
                WHERE unlocked_datetime IS NOT NULL
                ORDER BY unlocked_datetime DESC
            """)
        assignments = c.fetchall()
        parsed_assignments = []
        for ass in assignments:
            parsed_assignments.append({
                "id" : ass[0],
                "subject_type" : ass[1],
                "subject_id" : ass[2],
                "unlocked_datetime" : ass[3]
            })

        return( parsed_assignments )
