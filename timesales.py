#Script to download time and sales data from website https://quotes.hegnar.no/quotes/tradedump.php?
#Example of complete url  https://quotes.hegnar.no/quotes/tradedump.php?date=20181121&paper=SPY.A&csv_format=csv
#for SPY symobol
#the script is designed to be run daily as it updates the date value in the URL to today's date. 

import urllib.request as req
import datetime as dt

#create date formatted as YYYYMMDD
date = dt.datetime.now()

y = date.strftime("%Y")
m = date.strftime("%m")
d = date.strftime("%d")

#verify value is in expected format. E.q., 20181122
#print(y+m+d)

#create URL
url = 'https://quotes.hegnar.no/quotes/tradedump.php?date=' + y + m + d + '&paper=SPY.A&csv_format=csv'

#verify url is correct
#print (url)

#open the page and store the data in object named http. Then close connection
get_url = req.urlopen(url)
http = get_url.read()
get_url.close()

#verify the page looks correct
#print(http)

#create a file named ts + yyyymmdd and download it as csv since the data is already csv.
tnsfile = open('ts'+y+m+d+'.csv','wb')
tnsfile.write(http)

#Close connection to new file
tnsfile.close()
