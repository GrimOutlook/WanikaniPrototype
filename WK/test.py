from WanikaniSession import WanikaniSession

wk = WanikaniSession()

# wk.wk_db.purgeDatabase()
wk.importUserIntoDatabase()
wk.importAllCollectionsIntoDatabase()
#wk.downloadAllWKDataObjects()
