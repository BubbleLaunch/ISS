# Importing json and urlopen functions to pull ISS lat and lon data
# Also importing datetime function to time stamp lat and lon readings
import json
from urllib.request import urlopen
import datetime
import time
from math import cos, asin, sqrt, pi


##
# Prints Current ISS LATITUDE X

def isslat():
    # this code opens .json url and outputs the text data of current latitude as text
    url = "http://api.open-notify.org/iss-now.json"
    response = urlopen(url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    x = (data['iss_position']['latitude'])
    print(x)
    return x

##
# Prints Current ISS LONGITUDE Y

def isslon():
    # this code opens .json url and outputs the text data of current longitude as text
    url = "http://api.open-notify.org/iss-now.json"
    response = urlopen(url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    y = (data['iss_position']['longitude'])
    print(y)
    return y

##
# Writes the Lat and Lon of Iss to iss.txt with timestamp CST

f = open("iss.txt", "w")
for i in range(2):
    f.write("Iss longitude is ")
    f.write(isslon())
    f.write(" ")
    f.write("Iss latitude is ")
    f.write(isslat())
    f.write(" ")
    f.write(str(datetime.datetime.now()))
    f.write(" Central Standard Time")
    f.write('\n')
    time.sleep(1)


#if i == 2:
    #f = open("iss.txt", "r")
    #f.readline(1)
    #print(f.readline(-1))

def distance():
    url = "http://api.open-notify.org/iss-now.json"
    response = urlopen(url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    w = (data['iss_position']['latitude'])
    lat1 = float(w)
    url = "http://api.open-notify.org/iss-now.json"
    response = urlopen(url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    x = (data['iss_position']['latitude'])
    lat2 = float(x)
    url = "http://api.open-notify.org/iss-now.json"
    response = urlopen(url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    y = (data['iss_position']['longitude'])
    lon1 = float(y)
    url = "http://api.open-notify.org/iss-now.json"
    response = urlopen(url)
    contents = response.read()
    text = contents.decode('utf8')
    data = json.loads(text)
    z = (data['iss_position']['longitude'])
    lon2 = float(z)
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    13150 * asin(sqrt(a))
    print(a)
    return a




f = open("iss.txt", "w")
f.write("\n")
f.write("The distance travelled in KM ")
f.write(str(distance()))
f.close()











