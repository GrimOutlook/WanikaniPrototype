from WKObject import WKObject

class WKUser( WKObject ):
    def __init__( self, data, wk_db ):
        WKObject.__init__( self, data, wk_db )
        self.username                           = data["username"]
        self.level                              = data["level"]
        self.max_level_granted_by_subscription  = data["max_level_granted_by_subscription"]
        self.profile_url                        = data["profile_url"]
        self.started_datetime                   = data["started_datetime"]
        self.subscribed                         = data["subscribed"]
        self.current_vacation_started_datetime  = data["current_vacation_started_datetime"]
        self.subscription                       = data["subscription"]
        self.preferences                        = data["preferences"]

    @classmethod
    def fromAPI( self, data, wk_db ):
        d = r["data"]
        data = {
            "id"                                : d["id"],
            "object"                            : r["object"],
            "username"                          : d["username"],
            "level"                             : d["level"],
            "max_level_granted_by_subscription" : d["max_level_granted_by_subscription"],
            "profile_url"                       : d["profile_url"],
            "started_datetime"                  : d["started_at"],
            "subscribed"                        : str( d["subscribed"]),
            "current_vacation_started_datetime" : d["current_vacation_started_at"],
            "subscription"                      : str( d["subscription"]),
            "preferences"                       : str( d["preferences"])
        }
        cls( data, wk_db )

    def insertIntoDatabase( self ):
        sql = """ INSERT INTO user(
                id,
                object,
                username,
                level,
                max_level_granted_by_subscription,
                profile_url,
                started_datetime,
                subscribed,
                current_vacation_started_datetime,
                subscription,
                preferences
        )

        VALUES( ?,?,?,?,?,?,?,?,?,?,? ) """

        user = (
               self.id,
               self.object,
               self.username,
               self.level,
               self.max_level_granted_by_subscription,
               self.profile_url,
               self.started_datetime,
               self.subscribed,
               self.current_vacation_started_datetime,
               self.subscription,
               self.preferences
        )
        self.wk_db.sql_exec( sql, user )
