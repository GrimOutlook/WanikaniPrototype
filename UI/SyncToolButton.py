from PyQt5.Qt import *
from WK import SyncMode

class SyncToolButton( QToolButton ):
    def __init__( self, sync_mode ):
        super().__init__()
        self.setPopupMode( QToolButton.DelayedPopup )
        self.setText("Sync Mode")
        self.initMenu()

    def initMenu( self ):
        menu = QMenu()
        # menu.addAction( "Sync on review", self.setSyncMode( SyncMode.SYNC_ON_REVIEW ) )

    def setSyncMode( self, sync_mode ):
        self.sync_mode = sync_mode
