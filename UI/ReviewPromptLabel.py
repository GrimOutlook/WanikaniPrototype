from PyQt5.Qt import *

"""
##### TODO ####
1) Implement changing fonts and implement changing font on every new review item
2) Fix resizing, its okay right now, but might be made better with more effort
"""

class ReviewPromptLabel( QLabel ):
    def __init__( self, parent ):
        super().__init__(parent=parent)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def resizeEvent( self, e ):
        super(ReviewPromptLabel, self).resizeEvent( e )
        # print( "resizeEvent", e.size().width(), e.size().height() )
        QFrame.resizeEvent( self, e )
        font = self.font()
        if( self.width() * 0.40 < self.height() * 0.75 ):
            font.setPixelSize(self.width() * 0.40)
        else:
            font.setPixelSize(self.height() * 0.75)

        br = QFontMetrics( font ).boundingRect( self.text() )
        cr = self.contentsRect()
        # print( "BR: " + str(br.width()) + " x " + str( br.height()  ))
        # print( "CR: " + str(cr.width()) + " x " + str(cr.height()) + "\n" )


        self.setFont(font)

    # def resizeEvent(self, event):
        # super(ReviewPromptLabel, self).resizeEvent(event)

        # if not self.text():
            # return

        # # --- fetch current parameters ----

        # f = self.font()
        # cr = self.contentsRect()

        # # --- iterate to find the font size that fits the contentsRect ---

        # fs = f.pixelSize()
        # br = QFontMetrics(f).boundingRect(self.text())

        # if( br.height() < cr.height() and br.width() < cr.width() ):
            # while( br.height() < cr.height() and br.width() < cr.width() ):
                # fs += 1
                # f.setPixelSize(fs)
                # br = QFontMetrics(f).boundingRect(self.text())

            # f.setPixelSize(max(fs - 1, 1)) # backtrack

        # while( br.height() > cr.height() or br.width() > cr.width() ):
            # fs -= 1
            # f.setPixelSize(fs)
            # br = QFontMetrics(f).boundingRect(self.text())

        # # --- update font size ---      

        # self.setFont(f)
        # br = QFontMetrics( f ).boundingRect( self.text() )
        # cr = self.contentsRect()
        # print( "BR: " + str(br.width()) + " x " + str( br.height()  ))
        # print( "CR: " + str(cr.width()) + " x " + str(cr.height()) + "\n" )

