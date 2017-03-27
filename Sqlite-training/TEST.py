conn = sqlite3.connect('booli.db')
c = conn.cursor()
while offset < totalCount:
    # store data locally
    for apt in result['Sold']:
        # get or create sold object
        try:
            s = Sold.get(Sold.booliId == apt['booliId'])
        except Sold.DoesNotExist:
            s = Sold.create(
                booliId = apt['booliId'],
                  )
            s.save()
        # store area
        if ('namedAreas' in apt['location']):
            for areaName in apt['location']['namedAreas']:
                # get or create area object
                try:
                    a = Area.get(Area.name == areaName)
                except Area.DoesNotExist:
                    a = Area.create(name = areaName)
                    a.save()
                # get or create sold-area relationship
                try:
                    sa = SoldAreas.get(SoldAreas.sold == s, SoldAreas.area == a)
                except SoldAreas.DoesNotExist:
                    sa = SoldAreas.create(sold = s, area = a)
                    sa.save()
    print ("Stored data from ") + str(offset) + (" to ") + str(offset + limit) + (" of ") + str(totalCount)
    # query for next batch of listings
    offset += limit
    result = query(limit, offset)
    
conn.commit()

conn.close
