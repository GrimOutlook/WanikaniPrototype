import curses
import sys
sys.path.append("..")
sys.path.append("../WK")

from WanikaniSession import WanikaniSession
from ReviewSession import ReviewSession

"""
Probably need to check if necessary fonts are installed for language
"""
class WKTUI():
    def __init__( self ):
        self.scr = curses.initscr()
        self.scr.border()
        curses.cbreak()
        self.scr.keypad(False)
        curses.noecho()

        self.height, self.width = self.scr.getmaxyx()

        self.rs = ReviewSession()

    def drawReviewScreen( self ):
        try:
            k = 0

            curses.start_color()
            curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

            while( k != ord("~") ):
                # Get blank canvas
                self.scr.clear()
                self.height, self.width = self.scr.getmaxyx()

                self.drawKanji()
                self.drawRightStatsBar()
                self.drawStatusBar()

                # Refresh screen
                self.scr.refresh()
                # Wait for next input
                k = self.scr.getch()

        except KeyboardInterrupt:
            return

        except Exception as e:
            curses.endwin()
            print( e )

    def drawKanji( self ):
        try:
            " Will need to add check here to see if characters is none and will need to ignore radicals that only have pics"
            " A more far-fetched idea may use ascii text to create a representation of the image of the radical"
            kanji = self.rs.current_review_item.subject.characters
            kanji_x = int( (self.width//2) - (len(kanji)//2) - (len(kanji)%2) )
            kanji_y = int( (self.height//2) - 2 )

            # Add kanji text to screen
            self.scr.addstr( kanji_y, kanji_x, kanji )

        except KeyboardInterrupt:
            return

        except Exception as e:
            curses.endwin()
            print( e )

    def drawTopStatsBar( self ):
        try:
            total_reviews_left = self.rs.getTotalReviewsRemaining()
            total_done_reviews = self.rs.total_done_reviews
            percent_correct = self.rs.getPercentCorrectReviews()

            TRL_str = "Total: {}".format( total_reviews_left )
            TDR_str = "Done: {}".format( total_done_reviews )
            PC_str  = "Pct: {}".format( percent_correct )

            # 
            start_x = int( self.width - len( top_stats_bar_str ) )
            # We start the list at the top
            start_y = int( 0 )

            # 
            self.scr.addstr( start_y, start_x, TRL_str )
            self.scr.addstr( start_y+2, start_x, TDR_str )
            self.scr.addstr( start_y+4, start_x, PC_str )

        except KeyboardInterrupt:
            return

        except Exception as e:
            curses.endwin()
            print( e )

    def drawStatusBar( self ):
        try:
            # Render Status Bar
            statusbarstr = "Press '~' to exit | STATUS BAR"

            # Render status bar
            self.scr.attron(curses.color_pair(3))
            self.scr.addstr(self.height-1, 0, statusbarstr)
            self.scr.addstr(self.height-1, len(statusbarstr), " " * (self.width - len(statusbarstr) - 1))
            self.scr.attroff(curses.color_pair(3))

        except KeyboardInterrupt:
            return

        except Exception as e:
            curses.endwin()
            print( e )


    def __del__(self):
        curses.nocbreak()
        self.scr.keypad(False)
        curses.echo()
        curses.endwin()


def main():
    wktui = WKTUI()
    wktui.drawReviewScreen()

if __name__ == "__main__":
    main()
