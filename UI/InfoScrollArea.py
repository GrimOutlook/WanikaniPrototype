from PyQt5.Qt import *

class InfoScrollArea( QScrollArea ):
    def __init__( self, parent ):
        super().__init__( parent = parent )
        self.setAutoFillBackground(False)
        self.setWidgetResizable( True )
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("infoScrollArea")
        self.contents = QWidget()
        self.contents.setObjectName("mainScrollAreaWidgetContents")
        self.contents.setContentsMargins(0,0,0,0)

        self.setWidget(self.contents)

        self.mainInfoHLayout = QHBoxLayout()
        self.contents.setLayout( self.mainInfoHLayout )
        self.leftVerticalLayout = QVBoxLayout()
        self.mainInfoHLayout.addLayout( self.leftVerticalLayout )
        self.rightVerticalLayout = QVBoxLayout()
        self.mainInfoHLayout.addLayout( self.rightVerticalLayout )

    def hidePromptInfo( self, spacer ):
        self.removePreviousItemPromptInfo()
        self.hide()
        # This effectively begins showing the spacer again since the hide() and show() methods don't work on spacer objects
        spacer.changeSize( 0, 157, QSizePolicy.Minimum, QSizePolicy.Preferred )

    def showPromptInfo( self, review, question, spacer ):
        subject = review.subject.object

        if( subject == "kanji" ):
            self.createKanjiInfoContents( review, question )

        elif( subject == "vocabulary" ):
            self.createVocabularyInfoContents( review, question )

        self.show()
        # This effectivly hides the spacer since spacer objects cant use the hide() method
        spacer.changeSize(0,0,QSizePolicy.Ignored, QSizePolicy.Ignored)

    def createKanjiInfoContents( self, review, question ):
        if( question == "meaning" ):
            self.meaningInfoLabel = QLabel( "Meanings: {}".format( review.subject.getMeaningsString() ) )
            self.userSynonyms = QLabel( "User Synonyms" )
            self.radicalCombinations = QLabel( str(review.subject.amalgamation_subject_ids ))
            self.meaningMnemonicLabel = QLabel( review.subject.meaning_mnemonic )
            self.meaningHintLabel = QLabel( review.subject.meaning_hint )
            self.meaningNote = QLabel( "Meaning Note" )

            self.leftVerticalLayout.addWidget( self.meaningInfoLabel )
            self.leftVerticalLayout.addWidget( self.userSynonyms )
            self.leftVerticalLayout.addWidget( self.radicalCombinations )
            self.rightVerticalLayout.addWidget( self.meaningMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.meaningHintLabel )
            self.rightVerticalLayout.addWidget( self.meaningNote )

        elif( question == "reading" ):
            self.kunyomiLabel = QLabel( "Readings: {}".format( review.subject.getReadingsString() ) )
            self.radicalCombinations = QLabel( str(review.subject.amalgamation_subject_ids ))
            self.readingMnemonicLabel = QLabel( review.subject.reading_mnemonic )
            self.readingHintLabel = QLabel( review.subject.reading_hint )
            self.readingNote = QLabel( "Reading Note" )

            self.leftVerticalLayout.addWidget( self.kunyomiLabel )
            self.leftVerticalLayout.addWidget( self.radicalCombinations )
            self.rightVerticalLayout.addWidget( self.readingMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.readingHintLabel )
            self.rightVerticalLayout.addWidget( self.readingNote )

    def createVocabularyInfoContents( self, review, question ):
        if( question == "meaning" ):
            self.meaningInfoLabel = QLabel( "Meanings: {}".format( review.subject.getMeaningsString() ) )
            self.userSynonyms = QLabel( "User Synonyms" )
            self.partsOfSpeechLabel = QLabel( "Part of Speech: {}".format( review.subject.getPartsOfSpeechString() ) )
            self.relatedKanji = QLabel( str(review.subject.component_subject_ids ))
            self.meaningMnemonicLabel = QLabel( review.subject.meaning_mnemonic )
            self.meaningNote = QLabel( "Meaning Note" )

            self.leftVerticalLayout.addWidget( self.meaningInfoLabel )
            self.leftVerticalLayout.addWidget( self.userSynonyms )
            self.leftVerticalLayout.addWidget( self.partsOfSpeechLabel )
            self.leftVerticalLayout.addWidget( self.relatedKanji )
            self.rightVerticalLayout.addWidget( self.meaningMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.meaningNote )

        elif( question == "reading" ):
            self.readingInfoLabel = QLabel( "Readings: {}".format( review.subject.getReadingsString() ) )
            self.partsOfSpeechLabel = QLabel( "Part of Speech: {}".format( review.subject.getPartsOfSpeechString() ) )
            self.relatedKanji = QLabel( str(review.subject.component_subject_ids ))
            self.readingMnemonicLabel = QLabel( review.subject.reading_mnemonic )
            self.readingNote = QLabel( "Reading Note" )

            self.leftVerticalLayout.addWidget( self.readingInfoLabel )
            self.leftVerticalLayout.addWidget( self.partsOfSpeechLabel )
            self.leftVerticalLayout.addWidget( self.relatedKanji )
            self.rightVerticalLayout.addWidget( self.readingMnemonicLabel )
            self.rightVerticalLayout.addWidget( self.readingNote )

    def removePreviousItemPromptInfo( self ):
        for layout in [ self.leftVerticalLayout, self.rightVerticalLayout ]:
            for i in range( layout.count() ):
                obj = layout.takeAt( 0 ) # Removes the first object and puts it in obj, all other objects in layout are shifted down
                obj.widget().setVisible( False )
                obj = obj.widget() # del says it cant delete a function call so this must be done
                del obj

