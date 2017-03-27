import http.client
import hashlib
import time
import random
import string
import sqlite3
import json

callerId = "carladam.vs"
API_KEY = "DYmhWmIjJgaSAgduFFjs5OYgRD8ig1MGIZtx1Arq"

timestamp = str(int(time.time()))
unique = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(16))
hashstr=hashlib.sha1((callerId+timestamp+API_KEY+unique).encode()).hexdigest()
url = "/sold?q=vasastan&minLivingArea=90&maxConstructionYear=1930&callerId="+callerId+"&time="+timestamp+"&unique="+unique+"&hash="+hashstr
connection = http.client.HTTPConnection("api.booli.se")
connection.request("GET", url)
response = connection.getresponse()
data = response.read()
connection.close()
if response.status != 200:
    print ("fail")
print(type(data))
#need to convert bytes to string to decode using json -> test with #
datadecode=data.decode('utf-8')
#print(datadecode)
json.loads(datadecode)
#
#
