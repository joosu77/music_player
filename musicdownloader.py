from __future__ import unicode_literals
import urllib
import urllib2
from bs4 import BeautifulSoup
import youtube_dl
import gspread
from oauth2client.service_account import ServiceAccountCredentials

conf = open("config.txt","r")

path = conf.readline().split('"')[1]
sheetname = conf.readline().split('"')[1]

conf.close()

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def download(artist,name):
    ydl_opts["outtmpl"]= unicode(path+'/music/'+artist+'/'+name+'.mp3')
    
    query = urllib.quote(artist + " - " + name)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,'lxml') #viimase argumendi voib teistel platvormidel eemal
    vidHtml = "https://www.youtube.com" + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vidHtml])


ans = raw_input("sisendfail v google spreadsheets (f/s)?")
if ans=='f':
    sis = open('inpfile.txt','r')
    for line in sis:
        artist = line.split('@')[0]
        name = line.split('@')[1].strip()
        download(artist,name)
    sis.close()
        
else:
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    print sheetname
    sheet = client.open(sheetname).sheet1
    i = 2
    while len(sheet.cell(i,1).value):
        artist = sheet.cell(i,2).value
        name = sheet.cell(i,1).value
        download(artist,name)
        
        o = 3
        genres = []
        while len(sheet.cell(i,o).value):
            genres.append(sheet.cell(i,o).value)
            o = o+1
        for gen in genres:
            exists = True
            try:
                cache = open(path+"/genres/"+gen+".txt","a")
            except:
                cache = open(path+"/genres/"+gen+".txt","r")
                if any(text ==(name+"@"+artist) for text in cache):
                    cache.close()
                    cache = open(path+"/genres/"+gen+".txt","w")
                    exists = False
            if not exists:
                cache.write(name + "@" + artist+'\n')
                cache.close()
        i = i+1