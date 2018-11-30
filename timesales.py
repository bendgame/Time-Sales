#Script to download time and sales data from website https://quotes.hegnar.no/quotes/tradedump.php?
#Example of complete url  https://quotes.hegnar.no/quotes/tradedump.php?date=20181121&paper=SPY.A&csv_format=csv
#for SPY symobol
#the script is designed to be run daily as it updates the date value in the URL to today's date. 
#REPLACE the save_path string below with the path you want to save to.

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
#print (url)

#REPLACE #username in the save_path string below with the computer username before running.

#path to direct the saved file. 
#Using r before the string converts it to a raw string. 
#if you get this error, you did it wrong 
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#REPLACE the save_path string below with the path you want to save to.

save_path = r'C:\Users\username\Desktop\Algo\Spy Time Sales\spyTS'+y+m+d+'.csv'


#open the page and save it as an object named http
get_url = req.urlopen(url)
http = get_url.read()
get_url.close()

#create a file named ts + yyyymmdd and download it as csv since it is already a csv file. 
tnsfile = open(save_path,'wb')
tnsfile.write(http)

#close python connection to the file
tnsfile.close()
