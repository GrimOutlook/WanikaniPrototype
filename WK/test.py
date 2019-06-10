from WanikaniSession import WanikaniSession

wk = WanikaniSession()
obj = wk.getFromAPI(wk.BASE_API_URL + "subjects/1")
wk.importObjectIntoItemDatabase( obj, "s" )

obj = wk.getFromAPI(wk.BASE_API_URL + "subjects/440")
wk.importObjectIntoItemDatabase( obj, "s" )

obj = wk.getFromAPI(wk.BASE_API_URL + "subjects/2467")
wk.importObjectIntoItemDatabase( obj, "s" )

wk.importAllCollectionsIntoDatabase()
#wk.downloadAllWKDataObjects()
