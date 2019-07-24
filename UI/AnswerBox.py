"""
AnswerBox must take in the type of question and change its behavior to match.
While question type is meaning, it allows the standard english keyboard to work unchanged.
When the question type is reading the box then dynamically converts the text into hiragana and katakana
"""

from PyQt5.Qt import *

from PseudoJapaneseIME import PseudoJapaneseIME

class AnswerBox( QLineEdit ):
    def __init__( self, parent ):
        super().__init__(parent=parent)
        self.parent = parent

        self.IME = PseudoJapaneseIME()
        self.textChanged.connect( self.romanjiToKana )

        self.stylesheets = {
            "default"   :   "",
            "correct"   :   "background-color : green",
            "incorrect" :   "background-color : red",
            "ignored"   :   "background-color : yellow"
        }

    def setStyle( self, style ):
        self.setStyleSheet( self.stylesheets[ style ] )

    def romanjiToKana( self ):
        if( self.parent.rs.current_question == "reading" ):
            new_text = self.IME.romanjiToKana( self.text() )
            self.setText( new_text )

