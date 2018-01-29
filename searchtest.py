import urllib
import urllib2
from bs4 import BeautifulSoup

textToSearch = 'singer vinger raha'
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,'lxml') #viimase argumendi voib teistel platvormidel eemaldada, see on siin ainult warningu eemaldamiseks
print "https://www.youtube.com"+ soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']
#for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
#    print 'https://www.youtube.com' + vid['href']