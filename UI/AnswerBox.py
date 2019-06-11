"""
AnswerBox must take in the type of question and change its behavior to match.
While question type is meaning, it allows the standard english keyboard to work unchanged.
When the question type is reading the box then dynamically converts the text into hiragana and katakana
"""

from PyQt5.Qt import *

class AnswerBox( QLineEdit ):
    def __init__( self, parent ):
        super().__init__(parent=parent)
        self.parent = parent

    def keyPressEvent( self, e ):
        if( e.key() != Qt.Key_Backspace and self.parent.rs.current_question == "reading" ):
            # Parse english to japanese
            pass

        super().keyPressEvent(e)
