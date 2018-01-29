from __future__ import unicode_literals
import urllib
import urllib2
from bs4 import BeautifulSoup
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/home/joosep/proge/yt/%(artist)s/%(name)s.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


    #textToSearch = 'singer vinger raha'
sis = open('inpfile.txt','r')
for line in sis:
    artist = line.split('@')[0]
    name = line.split('@')[1].strip()
    ydl_opts["outtmpl"]= unicode('/home/joosep/proge/yt/'+artist+'/'+name+'.mp3')
    
    query = urllib.quote(artist + " - " + name)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'lxml') #viimase argumendi voib teistel platvormidel eemal
    vidHtml = "https://www.youtube.com" + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vidHtml])
