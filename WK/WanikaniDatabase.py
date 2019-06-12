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
        """

        sql_create_table_radical = """CREATE TABLE IF NOT EXISTS radical (
                id integer PRIMARY KEY,
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
                url text,
                filepath text
        );"""
        sql_create_table_review = """CREATE TABLE IF NOT EXISTS review (
                id integer PRIMARY KEY,
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
                created_datetime text,
                assignment_id integer,
                subject_id integer,
                incorrect_meaning_answers integer,
                incorrect_reading_answers integer
        );"""
        sql_create_table_assignment = """CREATE TABLE IF NOT EXISTS assignment (
                id integer PRIMARY KEY,
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
                subject_id integer,
                started_datetime text
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

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

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

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

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

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

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

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,? ) """

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
                assignment_id,
                subject_id,
                incorrect_meaning_answers,
                incorrect_reading_answers
        )

        VALUES( ?,?,?,?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, review )
        except Error as e:
            print(e)
            print( "Creating updated_review table entry failed..." )

    def createAssignment( self, assignment ):
        sql = """ INSERT INTO assignment(
                id,
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

        VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, assignment )
        except Error as e:
            print(e)
            print( "Creating assignment table entry failed..." )

    def createUpdatedAssignment( self, assignment ):
        sql = """ INSERT INTO updated_assignment(
                id,
                subject_id,
                started_datetime
        )

        VALUES( ?,?,? ) """

        try:
            c = self.conn.cursor()
            c.execute( sql, assignment )
        except Error as e:
            print(e)
            print( "Creating updated_assignment table entry failed..." )

    def createDownloadQueueItem( self, item_id, url, filepath ):
        sql = """ INSERT INTO download_queue(
                id,
                url,
                filepath
        )

        VALUES( ?,?,? ) """

        if( self.conn != None ):
            c = self.conn.cursor()

        try:
            c.execute( sql, (item_id, url, filepath) )
        except Error as e:
            print(e)
            print( "Creating download queue table entry failed..." )

    """
    ############################
    # Data gathering functions #
    ############################
    """
    def itemTypeIsValid( self, item_type ):
        valid_types = [ "radical", "kanji", "vocabulary", "review", "updated_review", "assignment", "updated_assignment", "download_queue" ]
        return ( item_type in valid_types )

    def objectExistsInDatabase( self, item_id, item_type ):
        return( len( self.getObjectByID( item_id, item_type ) ) > 0 )

    def getObjectByID( self, item_id, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.conn.cursor()
        c.execute( "SELECT * FROM {} WHERE id=?".format(item_type), (item_id,) )
        return( c.fetchall() )

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
        return( c.fetchall() )

    def getAllOfItemTypeFromTable( self, item_type ):
        if( not self.itemTypeIsValid( item_type ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.conn.cursor()
        c.execute( "SELECT * FROM {}".format(item_type ) )
        return( c.fetchall() )

    def removeFromTableByID( self, item_id, table ):
        if( not self.itemTypeIsValid( table ) ):
            raise Exception("Provided item type is not supported. Item is of type {}".format(item_type))

        c = self.conn.cursor()
        c.execute( "DELETE FROM {} WHERE id=?".format( table ), (item_id,) )

    def getValidReviewsFromList( self, l, index ):
        return( [ i for i in l if( i[ index ] != None and datetime.datetime.fromisoformat( i[ index ].strip("Z") ) < datetime.datetime.now() ) ] )

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
