#scraping the web for lyrics
import requests
import time
from bs4 import BeautifulSoup

url= "https://www.metrolyrics.com/the-1975-lyrics.html"
links = []

soup= BeautifulSoup(requests.get(url).text, "html.parser")
table= soup.find("table")
for song in table.find_all('a'):
    links.append(song.get("href"))
#print(links)

#Scrape the lyrics from each link
lyrics=[]
for link in links:
    time.sleep(0.1)
    bs= BeautifulSoup(requests.get(link).text, "html.parser")
    paras = bs.find_all('p')
    song_text=""
    for p in paras:
        if p.get("class") != None and "verse" in p.get("class"):
            song_text= song_text + p.text
    lyrics.append(song_text)
 
lyrics = [x.lower() for x in lyrics]
print(lyrics[0][:100])
#get song titles, store them in a list. Use url+artist+songtitle. Parse and get lyrics for each song
   
import pickle

pickle.dump(lyrics, open('lyrics.pkl', 'wb'))







