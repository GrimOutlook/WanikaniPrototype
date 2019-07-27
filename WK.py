from enum import Enum

class Pages( Enum ):
    MAIN_WINDOW = 0
    HOME_PAGE = 1
    REVIEW_PAGE = 2
    WANIKANI_DATABASE = 3
    WANIKANI_SESSION = 4
    REVIEW_SESSION = 5

class ReviewState( Enum ):
    READY_FOR_ANSWER = 0
    ANSWER_SHOWN = 1
    ANSWER_GIVEN = 2
    WAITING_FOR_INCORRECT_DELAY = 3

class ReviewMode( Enum ):
    TYPING = 0
    ANKI = 1

class WKColor():
    """
    Colors
    """
    APPRENTICE_PINK     = "#DD0099" # Normal pink, for apprentice
    GURU_PURPLE         = "#882D9E" # Normal purple, for guru
    MASTER_BLUE         = "#294DDB" # Normal dark blue, for master
    ENLIGHTENED_BLUE    = "#0093DD" # Normal light blue, for enlightened
    BURNED_GRAY         = "#555555" # Normal gray, for burned
    BURNED_GREY         = BURNED_GRAY

    RADICAL_BLUE        = "#0088CC" # light - "#00AAFF"
    KANJI_PINK          = "#CC0088" # light - "#FF00AA"
    VOCABULARY_PURPLE   = "#8800CC" # light - "#AA00FF"

    ANSWER_CORRECT      = "#88CC00"
    ANSWER_INCORRECT    = "#FF0033"

    ACCENT_GRAY   = "#242628" # light #D5D5D5 ; Used for the bacground of the progression items on the home page and as the headers for the lsits below it
    BACKGROUND_GRAY = "#393B3B" # light - #EFEFEF
    HOMEPAGE_HEADER = "181A1B" # light - F7F7F7

    RADICAL_PROGRESSION_MASK_BLUE = "#82B6CE" # This is just a guess that can be altered later
    RADICAL_PROGRESSION_DONE_BLUE = "#242C4C" # light -"#9AA5CF"
    KANJI_PROGRESSION_MASK_PINK = "#FF99DD" # Used for marking locked kanji in the level kanji progression
    KANJI_PROGRESSION_DONE_PINK = "#3A254B"
    DARK_GRAY   = "#1A1B1C"
    DARK_GREY   = DARK_GRAY
    BLACK       = DARK_GRAY


    """
    WanikaniSessoin modes
    """
    SINGLE_MODE = 0
    BULK_MODE = 1

class HomepageStatsCategories( Enum ):
    """
    Homepage Stats Categories
    """
    NEW_UNLOCKS = 0
    CRITICAL_CONDITION_ITEMS = 1
    RECENT_BURNED_ITEMS = 2

class HomepageStatsListItems( Enum ):
    """
    Homepage stats Poistion in List
    """
    TOP_LABEL = 0       # Resereved fot the top label which says what the stats represent such as "CRITICAL CONDITION ITEMS"
    BOTTOM_LABEL = 1    # Reserved for the "SEE MORE ___" labels at the bottom of stats lists

class TerminalColorPalette():
    DEFAULT_HIGHLIGHT    = 1
    CORRECT_ANSWER_BOX   = 2
    INCORRECT_ANSWER_BOX = 3
    IGNORED_ANSWER_BOX   = 4
    MEANING_QUESTION     = 5
    READING_QUESTION     = 6
    REVIEW_VOCABULARY    = 7
    REVIEW_KANJI         = 8

class TerminalColors():
    RADICAL_BLUE        = 33
    KANJI_PINK          = 198
    VOCABULARY_PURPLE   = 93
    CORRECT_GREEN       = 46
    INCORRECT_RED       = 196
    IGNORED_YELLOW      = 226
    MEANING_WHITE       = 250
    READING_BLACK       = 237

class SRSStages():
    INITIATE        = 0
    APPRENTICE_I    = 1
    APPRENTICE_II   = 2
    APPRENTICE_III  = 3
    APPRENTICE_IV   = 4
    GURU_I          = 5
    GURU_II         = 6
    MASTER          = 7
    ENLIGHTENED     = 8
    BURNED          = 9
