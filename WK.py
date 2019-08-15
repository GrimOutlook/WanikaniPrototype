from enum import Enum

class Pages():
    MAIN_WINDOW         = 0
    HOME_PAGE           = 1
    REVIEW_PAGE         = 2
    WANIKANI_DATABASE   = 3
    WANIKANI_SESSION    = 4
    REVIEW_SESSION      = 5

class ReviewState():
    READY_FOR_ANSWER    = 0
    ANSWER_SHOWN        = 1
    ANSWER_GIVEN        = 2
    WAITING_FOR_INCORRECT_DELAY = 3

class ReviewMode():
    TYPING          = 0
    ANKI            = 1
    ANKI_W_BUTTONS  = 2

class WKColor():
    """
    Colors
    """
    APPRENTICE_PINK     = "#DD0099" # Normal pink, for apprentice
    GURU_PURPLE         = "#882D9E" # Normal purple, for guru
    MASTER_BLUE         = "#294DDB" # Normal dark blue, for master
    ENLIGHTENED_BLUE    = "#0093DD" # Normal light blue, for enlightened
    BURNED_GRAY = BURNED_GREY = "#555555" # Normal gray, for burned

    RADICAL_BLUE        = "#0088CC" # light - "#00AAFF"
    KANJI_PINK          = "#CC0088" # light - "#FF00AA"
    VOCABULARY_PURPLE   = "#8800CC" # light - "#AA00FF"

    ANSWER_CORRECT      = "#88CC00"
    ANSWER_INCORRECT    = "#FF0033"

    ACCENT_GRAY     = "#242628" # light #D5D5D5 ; Used for the bacground of the progression items on the home page and as the headers for the lsits below it
    BACKGROUND_GRAY = "#393B3B" # light - #EFEFEF
    HOMEPAGE_HEADER = "181A1B" # light - F7F7F7

    RADICAL_PROGRESSION_MASK_BLUE   = "#82B6CE" # This is just a guess that can be altered later
    RADICAL_PROGRESSION_DONE_BLUE   = "#242C4C" # light -"#9AA5CF"
    KANJI_PROGRESSION_MASK_PINK     = "#FF99DD" # Used for marking locked kanji in the level kanji progression
    KANJI_PROGRESSION_DONE_PINK     = "#3A254B"
    BLACK = DARK_GRAY = DARK_GRAY   = "#1A1B1C"


    """
    WanikaniSessoin modes
    """
    SINGLE_MODE = 0
    BULK_MODE   = 1

class HomepageStatsCategories():
    """
    Homepage Stats Categories
    """
    NEW_UNLOCKS                 = 0
    CRITICAL_CONDITION_ITEMS    = 1
    RECENT_BURNED_ITEMS         = 2

class HomepageStatsListItems():
    """
    Homepage stats Poistion in List
    """
    TOP_LABEL       = 0    # Resereved fot the top label which says what the stats represent such as "CRITICAL CONDITION ITEMS"
    BOTTOM_LABEL    = 1    # Reserved for the "SEE MORE ___" labels at the bottom of stats lists

class TerminalColorPalette():
    DEFAULT_HIGHLIGHT    = 1
    CORRECT_ANSWER_BOX   = 2
    INCORRECT_ANSWER_BOX = 3
    IGNORED_ANSWER_BOX   = 4
    MEANING_QUESTION     = 5
    READING_QUESTION     = 6
    REVIEW_VOCABULARY    = 7
    REVIEW_KANJI         = 8
    REVIEW_RADICAL       = 9
    APPRENTICE_PINK      = 10
    GURU_PURPLE          = 11
    MASTER_BLUE          = 12
    ENLIGHTENED_BLUE     = 13
    BURNED_GRAY          = 14

class TerminalColors():
    RADICAL_BLUE        = 33
    KANJI_PINK          = 198
    VOCABULARY_PURPLE   = 93
    CORRECT_GREEN       = 46
    INCORRECT_RED       = 196
    IGNORED_YELLOW      = 226
    MEANING_WHITE       = 250
    READING_BLACK       = 237
    APPRENTICE_PINK     = 198
    GURU_PURPLE         = 93
    MASTER_BLUE         = 27
    ENLIGHTENED_BLUE    = 33
    BURNED_GRAY         = 237

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

class SortMode():
    RANDOM  = 0
    SRS     = 1
    SUBJECT = 2
    LEVEL   = 3

class SyncMode():
    SYNC_ON_REVIEW  = 0
    DELAY_SYNC      = 1 # This allows for users to ignore reviews earlier than just the previous review
    NO_SYNC         = 2 # Doesn't sync whilst doing reviews, users must manually hit the sync button
