#Script to download time and sales data from website https://quotes.hegnar.no/quotes/tradedump.php?date=20181121&paper=SPY.A&csv_format=csv
#for SPY 
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
url = ['https://quotes.hegnar.no/quotes/tradedump.php?date=' + y + m + d + '&paper=SPY.A&csv_format=csv']
print (url)

#open the page and close connection
get_url = req.urlopen(url)
http = get_url.read()
get_url.close()

#verify the page looks correct
print(http)

