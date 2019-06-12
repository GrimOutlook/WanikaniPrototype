class PseudoJapaneseIME():
    def __init__( self ):
        self.mappings = [
            [ "a", "あ", "ア" ], [ "i", "い", "イ" ], [ "u", "う", "ウ" ], [ "e", "え", "エ" ], [ "o", "お", "オ" ],
            [ "ka", "か", "カ" ],   [ "ki" , "き", "キ" ],   [ "ku", "く", "ク" ], [ "ke" , "け", "ケ" ], [ "ko", "こ", "コ" ],
            [ "sa", "さ", "サ" ],   [ "shi", "し", "シ" ],   [ "si", "し", "シ" ], [ "su" , "す", "ス" ], [ "se", "せ", "セ" ], [ "so", "そ", "ソ" ],
            [ "ta", "た", "タ" ],   [ "chi", "ち", "チ" ],   [ "ti", "ち", "チ" ], [ "tsu", "つ", "ツ" ], [ "tu", "つ", "ツ" ], [ "te", "て", "テ" ], [ "to", "と", "ト" ],
            [ "na", "な", "ナ" ],   [ "ni" , "に", "ニ" ],   [ "nu", "ぬ", "ヌ" ], [ "ne" , "ね", "ネ" ], [ "no", "の", "ノ" ],
            [ "ha", "は", "ハ" ],   [ "hi" , "ひ", "ヒ" ],   [ "hu", "ふ", "フ" ], [ "fu" , "ふ", "フ" ], [ "he", "へ", "ヘ" ], [ "ho", "ほ", "ホ" ],
            [ "ma", "ま", "マ" ],   [ "mi" , "み", "ミ" ],   [ "mu", "む", "ム" ], [ "me" , "め", "メ" ], [ "mo", "も", "モ" ],
            [ "ya", "や", "ヤ" ],   [ "yu" , "ゆ", "ユ" ],   [ "yo", "よ", "ヨ" ],
            [ "ra", "ら", "ラ" ],   [ "ri" , "り", "リ" ],   [ "ru", "る", "ル" ], [ "re" , "れ", "レ" ], [ "ro", "ろ", "ロ" ],
            [ "wa", "わ", "ワ" ],   [ "wo" , "を", "ヲ" ],   [ "nn", "ん", "ン" ],
            [ "ga", "が", "ガ" ],   [ "gi" , "ぎ", "ギ" ],   [ "gu", "ぐ", "グ" ], [ "ge" , "げ", "ゲ" ], [ "go", "ご", "ゴ" ],
            [ "za", "ざ", "ザ" ],   [ "ji" , "じ", "ジ" ],   [ "zu", "ず", "ズ" ], [ "ze" , "ぜ", "ゼ" ], [ "zo", "ぞ", "ゾ" ],
            [ "da", "だ", "ダ" ],   [ "ti" , "ぢ", "ヂ" ],   [ "du", "づ", "ヅ" ], [ "de" , "で", "デ" ], [ "do", "ど", "ド" ],
            [ "ba", "ば", "バ" ],   [ "bi" , "び", "ビ" ],   [ "bu", "ぶ", "ブ" ], [ "be" , "べ", "ベ" ], [ "bo", "ぼ", "ボ" ],
            [ "pa", "ぱ", "パ" ],   [ "pi" , "ぴ", "ピ" ],   [ "pu", "ぷ", "プ" ], [ "pe" , "ぺ", "ペ" ], [ "po", "ぽ", "ポ" ],
            [ "kya"  , "きゃ"   , "キャ" ], [ "kyu" , "きゅ"    , "キュ" ], [ "kyo" , "きょ"    , "キョ" ],
            [ "gya"  , "ぎゃ"   , "ギャ" ], [ "gyu" , "ぎゅ"    , "ギュ" ], [ "gyo" , "ぎょ"    , "ギョ" ],
            [ "nya"  , "にゃ"   , "ニャ" ], [ "nyu" , "にゅ"    , "ニュ" ], [ "nyo" , "にょ"    , "ニョ" ],
            [ "hya"  , "ひゃ"   , "ヒャ" ], [ "hyu" , "ひゅ"    , "ヒュ" ], [ "hyo" , "ひょ"    , "ヒョ" ],
            [ "bya"  , "びゃ"   , "ビャ" ], [ "byu" , "びゅ"    , "ビュ" ], [ "byo" , "びょ"    , "ビョ" ],
            [ "pya"  , "ぴゃ"   , "ピャ" ], [ "pyu" , "ぴゅ"    , "ピュ" ], [ "pyo" , "ぴょ"    , "ピョ" ],
            [ "mya"  , "みゃ"   , "ミャ" ], [ "myu" , "みゅ"    , "ミュ" ], [ "myo" , "みょ"    , "ミョ" ],
            [ "rya"  , "りゃ"   , "リャ" ], [ "ryu" , "りゅ"    , "リュ" ], [ "ryo" , "りょ"    , "リョ" ],
            [ "ja"   , "じゃ"   , "ジャ" ], [ "ju"  , "じゅ"    , "ジュ" ], [ "je"  , "じぇ"    , "ジェ" ], [ "jo"   , "じょ"    , "ジョ" ],
            [ "cha"  , "ちゃ"   , "チャ" ], [ "chu" , "ちゅ"    , "チュ" ], [ "che" , "ちぇ"    , "チェ" ], [ "cho"  , "ちょ"    , "チョ" ],
            [ "sha"  , "しゃ"   , "シャ" ], [ "shu" , "しゅ"    , "シュ" ], [ "she" , "しぇ"    , "シェ" ], [ "sho"  , "しょ"    , "ショ" ]
        ]
        self.sokuon = {
            "english" : ["kk", "ss", "cc", "tt", "pp"],
            "sokuon" : "っ",
            "sokuon_cap" : "ッ"
        }

    def romanjiToKana( self, text ):
        slices = [ text[ -1 : ] ]
        if( len(text) >= 2 ):
            # Slices the last 2 characters
            slices.insert( 0, text[ -2 : ] )

        if( len(text) >= 3 ):
            # Slices the last 3 characters
            slices.insert( 0, text[ -3 : ] )

        for sl in slices:
            for mapp in self.mappings:
                if( sl == mapp[0] ):
                    new_text = text.replace( sl, mapp[1] )
                    return(new_text)

                elif( sl == mapp[0].upper() ):
                    new_text = text.replace( sl, mapp[2] )
                    return(new_text)

            for item in self.sokuon["english"]:
                if( sl == item ):
                    new_text = text.replace( sl, self.sokuon["sokuon"] ) + sl[0]
                    return( new_text )

                elif( sl == item.upper() ):
                    new_text = text.replace( sl, self.sokuon["sokuon_cap"] ) + sl[0]
                    return( new_text )

        return( text )
