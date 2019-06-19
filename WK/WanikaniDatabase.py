import sqlite3
from sqlite3 import Error

import datetime # For calculating timestamps
import ast # This is for converting the returned database info into dictonaries easier

from settings import Settings

class WanikaniDatabase():
    def __init__( self, database_filename="/home/dom/Code/Projects/WanikaniPrototype/wanikani.db" ):

        self.settings = Settings( "wanikani_database" )
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
                id integer PRIMARY KEY,
                object text,
                created_datetime text,
                assignment_id integer,
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

        self.database_filename = database_filename
        # path can equal either :memory: or a database file
        try:
            self.conn = sqlite3.connect( self.database_filename )
        except Error as e:
            print( e )
            self.conn.close()
            print("Connection to database failed. Closing...")
            exit()

        self.create_table( sql_create_table_radical )
        self.create_table( sql_create_table_kanji )
        self.create_table( sql_create_table_vocabulary )
        self.create_table( sql_create_table_download_queue )
        self.create_table( sql_create_table_review )
        self.create_table( sql_create_table_updated_review )
        self.create_table( sql_create_table_assignment )
        self.create_table( sql_create_table_updated_assignment )
        self.create_table( sql_create_table_user )
        self.commitChanges()

    def commitChanges( self ):
        self.conn.commit()

    def create_table( self, create_table_sql ):
        try:
            c = self.conn.cursor()
            c.execute( create_table_sql )
        except Error as e:
            print(e)
            print( "Creating SQL table failed..." )

    def purgeDatabase( self ):
        if( self.database_filename != ":memory:" ):
            os.remove( self.database_filename )
        else:
            self.conn.close()
            self.conn.connect( self.database_filename )


    """
    ############################
    # Data insertion Functions #
    ############################
    """

    def createRadical( self, radical ):
        sql = """ INSERT INTO radical(
                id,
                object,
                api_url,
                last_updated_datetime,
                amalgamation_subject_ids,
                auxiliary_meanings,
                characters,
                character_images_info,
                character_images_path,
                created_datetime,
                document_url,
                hidden_datetime,
                lesson_position,
                level,
                meanings,
                meaning_mnemonic,
                slug
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        if( self.conn != None ):
            c = self.conn.cursor()
        try:
            c.execute( sql, radical )
        except Error as e:
            print(e)
            print( "Creating radical table entry failed..." )


    def createKanji( self, kanji ):
        sql = """ INSERT INTO kanji(
                id,
                object,
                api_url,
                last_updated_datetime,
                amalgamation_subject_ids,
                auxiliary_meanings,
                characters,
                component_subject_ids,
                created_datetime,
                document_url,
                hidden_datetime,
                lesson_position,
                level,
                meanings,
                meaning_hint,
                meaning_mnemonic,
                readings,
                reading_mnemonic,
                reading_hint,
                slug,
                visually_similar_subject_ids
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        if( self.conn != None ):
            c = self.conn.cursor()

        try:
            c.execute( sql, kanji )
        except Error as e:
            print(e)
            print( "Creating kanji table entry failed..." )

    def createVocabulary( self, vocab ):
        sql = """ INSERT INTO vocabulary(
                id,
                object,
                api_url,
                last_updated_datetime,
                auxiliary_meanings,
                characters,
                component_subject_ids,
                context_sentences,
                created_datetime,
                document_url,
                hidden_datetime,
                lesson_position,
                level,
                meanings,
                meaning_mnemonic,
                parts_of_speech,
                pronunciation_audio_info,
                pronunciation_audio_path,
                readings,
                reading_mnemonic,
                slug
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        if( self.conn != None ):
            c = self.conn.cursor()

        try:
            c.execute( sql, vocab )
        except Error as e:
            print(e)
            print( "Creating vocabulary table entry failed..." )

    def createReview( self, review ):
        sql = """ INSERT INTO review(
                id,
                object,
                api_url,
                last_updated_datetime,
                created_datetime,
                assignment_id,
                subject_id,
                starting_srs_stage,
                starting_srs_stage_name,
                ending_srs_stage,
                ending_srs_stage_name,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, review )
        except Error as e:
            print(e)
            print( "Creating review table entry failed..." )

    def createUpdatedReview( self, review ):
        # This is all that is needed to post a review to wanikani
        sql = """ INSERT INTO updated_review(
                created_datetime,
                object,
                assignment_id,
                subject_id,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, review )
        except Error as e:
            print(e)
            print( "Creating updated_review table entry failed..." )

    def createAssignment( self, assignment ):
        sql = """ INSERT INTO assignment(
                id,
                object,
                api_url,
                last_updated_datetime,
                created_datetime,
                subject_id,
                subject_type,
                srs_stage,
                srs_stage_name,
                unlocked_datetime,
                started_datetime,
                passed_datetime,
                burned_datetime,
                available_datetime,
                resurrected_datetime,
                passed,
                resurrected,
                hidden
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, assignment )
        except Error as e:
            print(e)
            print( "Creating assignment table entry failed..." )

    def createUpdatedAssignment( self, assignment ):
        sql = """ INSERT INTO updated_assignment(
                id,
                object,
                subject_id,
                started_datetime
        )

        VALUES( ?,?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, assignment )
        except Error as e:
            print(e)
            print( "Creating updated_assignment table entry failed..." )

    def createDownloadQueueItem( self, item_id, obj, url, filepath ):
        sql = """ INSERT INTO download_queue(
                id,
                object,
                url,
                filepath
        )

        VALUES( ?,?,?,? ) """

        if( self.conn != None ):
            c = self.conn.cursor()

        try:
            c.execute( sql, (item_id, obj, url, filepath) )
        except Error as e:
            print(e)
            print( "Creating download queue table entry failed..." )

    def createUser( self, user ):
        sql = """ INSERT INTO user(
                id,
                object,
                username,
                level,
                max_level_granted_by_subscription,
                profile_url,
                started_datetime,
                subscribed,
                current_vacation_started_datetime,
                subscription,
                preferences
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,? ) """

        if( self.conn != None ):
            c = self.conn.cursor()

        try:
            c.execute( sql, user )
        except Error as e:
            print(e)
            print( "Creating download queue table entry failed..." )

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

        c = self.conn.cursor()
        c.execute( "SELECT * FROM {} WHERE id=?".format(item_type), (item_id,) )
        return( len( c.fetchall() ) > 0 )

    def getUserCurrentLevel( self ):
        level = self.getAllOfItemTypeFromTable( "user" )[0]["level"]
        return( level )

    def getSubjectObjectsOfGivenLevel( self, subject_type, level ):
        if( self.itemTypeIsValid( subject_type ) ):
            c = self.conn.cursor()
            c.execute( "SELECT * FROM {} WHERE level=?".format( subject_type ), (level,))
            return( self.parseDataList( c.fetchall() ) )

    def getAssignmentsBySRSStageName( self, level ):
        c = self.conn.cursor()
        c.execute( "SELECT * FROM assignment WHERE srs_stage_name=?", (level,))
        return( self.parseDataList( c.fetchall() ) )

    def getObjectByID( self, item_id, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.conn.cursor()
        c.execute( "SELECT * FROM {} WHERE id=?".format(item_type), (item_id,) )
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

        c = self.conn.cursor()
        c.execute( "SELECT * FROM {0} WHERE {1}=?".format(item_type, item_id_prompt[ item_type ]), (item_subject_id,) )
        return( self.parseData( c.fetchone() ) )

    def getAllOfItemTypeFromTable( self, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.conn.cursor()
        c.execute( "SELECT * FROM {}".format(item_type ) )
        return( self.parseDataList( c.fetchall() ) )

    def removeFromTableByID( self, item_id, table ):
        if( not self.itemTypeIsValid( table ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.conn.cursor()
        c.execute( "DELETE FROM {} WHERE id=?".format( table ), (item_id,) )

    def getValidReviewsFromList( self, l, index ):
        return( [ i for i in l if( i[ index ] != None and datetime.datetime.fromisoformat( i[ index ].strip("Z") ) < datetime.datetime.now() ) ] )

    def parseData( self, data ):
        obj = data[1]

        if( obj == "radical" ):
            parsed_obj = {
                "id"                        : data[0],
                "object"                    : data[1],
                "api_url"                   : data[2],
                "last_updated_datetime"     : data[3],
                "amalgamation_subject_ids"  : ast.literal_eval( data[4] ),
                "auxilary_meanings"         : ast.literal_eval( data[5] ),
                "characters"                : data[6],
                "character_images_info"     : data[7],
                "character_images_path"     : data[8],
                "created_datetime"          : data[9],
                "document_url"              : data[10],
                "hidden_datetime"           : data[11],
                "lesson_position"           : data[12],
                "level"                     : data[13],
                "meanings"                  : ast.literal_eval( data[14] ),
                "meaning_mnemonic"          : data[15],
                "slug"                      : data[16]
            }
        elif( obj == "kanji" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "api_url"                       : data[2],
                "last_updated_datetime"         : data[3],
                "amalgamation_subject_ids"      : ast.literal_eval( data[4] ),
                "auxilary_meanings"             : ast.literal_eval( data[5] ),
                "characters"                    : data[6],
                "component_subject_ids"         : ast.literal_eval( data[7] ),
                "created_datetime"              : data[8],
                "document_url"                  : data[9],
                "hidden_datetime"               : data[10],
                "lesson_position"               : data[11],
                "level"                         : data[12],
                "meanings"                      : ast.literal_eval( data[13] ),
                "meaning_hint"                  : data[14],
                "meaning_mnemonic"              : data[15],
                "readings"                      : ast.literal_eval( data[16] ),
                "reading_mnemonic"              : data[17],
                "reading_hint"                  : data[18],
                "slug"                          : data[19],
                "visually_similar_subject_ids"  : ast.literal_eval( data[20] )
            }
        elif( obj == "vocabulary" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "api_url"                       : data[2],
                "last_updated_datetime"         : data[3],
                "auxilary_meanings"             : ast.literal_eval( data[4] ),
                "characters"                    : data[5],
                "component_subject_ids"         : ast.literal_eval( data[6] ),
                "context_scentences"            : ast.literal_eval( data[7] ),
                "created_datetime"              : data[8],
                "document_url"                  : data[9],
                "hidden_datetime"               : data[10],
                "lesson_position"               : data[11],
                "level"                         : data[12],
                "meanings"                      : ast.literal_eval( data[13] ),
                "meaning_mnemonic"              : data[14],
                "parts_of_speech"               : ast.literal_eval( data[15] ),
                "pronunciation_audio_info"      : data[16],
                "pronunciation_audio_path"      : data[17],
                "readings"                      : ast.literal_eval( data[18] ),
                "reading_mnemonic"              : data[19],
                "slug"                          : data[20]
            }
        elif( obj == "download_item" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "url"                           : data[2],
                "filepath"                      : data[3]
            }
        elif( obj == "review" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "api_url"                       : data[2],
                "last_updated_datetime"         : data[3],
                "created_datetime"              : data[4],
                "assignment_datetime"           : data[5],
                "subject_id"                    : data[6],
                "starting_srs_stage"            : data[7],
                "starting_srs_stage_name"       : data[8],
                "ending_srs_stage"              : data[9],
                "ending_srs_stage_name"         : data[10],
                "incorrect_meaning_answers"     : data[11],
                "incorrect_reading_answers"     : data[12]
            }
        elif( obj == "updated_review" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "created_datetime"              : data[2],
                "assignment_id"                 : data[3],
                "subject_id"                    : data[4],
                "incorrect_meaning_answers"     : data[5],
                "incorrect_reading_answers"     : data[6]
            }
        elif( obj == "assignment" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "api_url"                       : data[2],
                "last_updated_datetime"         : data[3],
                "created_datetime"              : data[4],
                "subject_id"                    : data[5],
                "subject_type"                  : data[6],
                "srs_stage"                     : data[7],
                "srs_stage_name"                : data[8],
                "unlocked_datetime"             : data[9],
                "started_datetime"              : data[10],
                "passed_datetime"               : data[11],
                "burned_datetime"               : data[12],
                "available_datetime"            : data[13],
                "resurrected_datetime"          : data[14],
                "passed"                        : bool( data[15] ),
                "resurrected"                   : bool( data[16] ),
                "hidden"                        : bool( data[17] )
            }
        elif( obj == "updated_assignment" ):
            parsed_obj = {
                "id"                            : data[0],
                "object"                        : data[1],
                "subject_id"                    : data[2],
                "started_datetime"              : data[3]
            }
        elif( obj == "user" ):
            parsed_obj = {
                "id"                                : data[0],
                "object"                            : data[1],
                "username"                          : data[2],
                "level"                             : data[3],
                "max_level_granted_by_subscription" : data[4],
                "profile_url"                       : data[5],
                "started_datetime"                  : data[6],
                "subscribed"                        : bool( data[7] ),
                "current_vacation_started_datetime" : data[8],
                "subscription"                      : ast.literal_eval( data[9] ),
                "preferences"                       : ast.literal_eval( data[10] )
            }
        else:
            raise Exception( "Cannot parse object of unknown type. Object is of type {}".format(obj) )

        return( parsed_obj )


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

        ## Radicals
        :amalgamation_subject_ids:
        :auxilary_meanings:
        :characters:
        :character_images_path:
        :level:
        :meaning:
        :meaning_mnemonic:

        ## Kanji

        """

        reviews = []

        c = self.conn.cursor()
        c.execute(
            """ SELECT
                    assignment.id,
                    assignment.subject_id,
                    assignment.subject_type,
                    assignment.srs_stage_name,
                    assignment.available_datetime,
                    radical.amalgamation_subject_ids,
                    radical.auxiliary_meanings,
                    radical.characters,
                    radical.character_images_path,
                    radical.level,
                    radical.meanings,
                    radical.meaning_mnemonic

                FROM assignment INNER JOIN radical ON assignment.subject_id = radical.id
            """)
        radicals = self.getValidReviewsFromList( c.fetchall(), 4 )
        for item in radicals:
            reviews.append({
                "assignment_id"             : item[0],
                "subject_id"                : item[1],
                "subject_type"              : item[2],
                "srs_stage_name"            : item[3],
                "available_datetime"        : item[4],
                "amalgamation_subject_ids"  : ast.literal_eval( item[5] ),
                "auxilary_meanings"         : ast.literal_eval( item[6] ),
                "characters"                : item[7],
                "character_images_path"     : item[8],
                "level"                     : item[9],
                "meanings"                  : ast.literal_eval( item[10] ),
                "meaning_mnemonic"          : item[11],
                "incorrect_meaning_answers" : 0,
                "incorrect_reading_answers" : 0,
                "meaning_answers_done"      : False,
                "reading_answers_done"      : False,
                "completed_datetime"        : ""
            })


        c.execute(
            """ SELECT
                    assignment.id,
                    assignment.subject_id,
                    assignment.subject_type,
                    assignment.srs_stage_name,
                    assignment.available_datetime,
                    kanji.amalgamation_subject_ids,
                    kanji.auxiliary_meanings,
                    kanji.characters,
                    kanji.component_subject_ids,
                    kanji.level,
                    kanji.meanings,
                    kanji.meaning_hint,
                    kanji.meaning_mnemonic,
                    kanji.readings,
                    kanji.reading_mnemonic,
                    kanji.reading_hint,
                    kanji.visually_similar_subject_ids

                FROM assignment INNER JOIN kanji ON assignment.subject_id = kanji.id
            """)
        kanji = self.getValidReviewsFromList( c.fetchall(), 4 )
        for item in kanji:
            reviews.append({
                "assignment_id"                 : item[0],
                "subject_id"                    : item[1],
                "subject_type"                  : item[2],
                "srs_stage_name"                : item[3],
                "available_datetime"            : item[4],
                "amalgamation_subject_ids"      : ast.literal_eval( item[5] ),
                "auxilary_meanings"             : ast.literal_eval( item[6] ),
                "characters"                    : item[7],
                "component_subject_ids"         : ast.literal_eval( item[8] ),
                "level"                         : item[9],
                "meanings"                      : ast.literal_eval( item[10] ),
                "meaning_hint"                  : item[11],
                "meaning_mnemonic"              : item[12],
                "readings"                      : ast.literal_eval( item[13] ),
                "reading_mnemonic"              : item[14],
                "reading_hint"                  : item[15],
                "visually_similar_subject_ids"  : ast.literal_eval( item[16] ),
                "incorrect_meaning_answers" : 0,
                "incorrect_reading_answers" : 0,
                "meaning_answers_done"      : False,
                "reading_answers_done"      : False,
                "completed_datetime"        : ""
            })

        c.execute(
            """ SELECT
                    assignment.id,
                    assignment.subject_id,
                    assignment.subject_type,
                    assignment.srs_stage_name,
                    assignment.available_datetime,
                    vocabulary.auxiliary_meanings,
                    vocabulary.characters,
                    vocabulary.component_subject_ids,
                    vocabulary.context_sentences,
                    vocabulary.level,
                    vocabulary.meanings,
                    vocabulary.meaning_mnemonic,
                    vocabulary.parts_of_speech,
                    vocabulary.pronunciation_audio_path,
                    vocabulary.readings,
                    vocabulary.reading_mnemonic

                FROM assignment INNER JOIN vocabulary ON assignment.subject_id = vocabulary.id
            """)
        vocabulary = self.getValidReviewsFromList( c.fetchall(), 4 )
        for item in vocabulary:
            reviews.append({
                "assignment_id"                 : item[0],
                "subject_id"                    : item[1],
                "subject_type"                  : item[2],
                "srs_stage_name"                : item[3],
                "available_datetime"            : item[4],
                "auxilary_meanings"             : ast.literal_eval( item[5] ),
                "characters"                    : item[6],
                "component_subject_ids"         : ast.literal_eval( item[7] ),
                "context_sentences"             : ast.literal_eval( item[8] ),
                "level"                         : item[9],
                "meanings"                      : ast.literal_eval( item[10] ),
                "meaning_mnemonic"              : item[11],
                "parts_of_speech"               : ast.literal_eval( item[12] ),
                "pronunciation_audio_path"      : item[13],
                "readings"                      : ast.literal_eval( item[14] ),
                "reading_mnemonic"              : item[15],
                "incorrect_meaning_answers" : 0,
                "incorrect_reading_answers" : 0,
                "meaning_answers_done"      : False,
                "reading_answers_done"      : False,
                "completed_datetime"        : ""
            })

        return(reviews)

    def getUpdatedReviews( self ):
        updated_reviews = []
        c = self.conn.cursor()
        unparsed_updated_reviews = c.execute("SELECT * from updated_review").fetchall()
        for item in unparsed_updated_reviews:
            update_reviews.append({
                "completed_datetime"        : item[0],
                "assignment_id"             : item[1],
                "subject_id"                : item[2],
                "incorrect_meaning_answers" : item[3],
                "incorrect_reading_answers" : item[4]
            })
