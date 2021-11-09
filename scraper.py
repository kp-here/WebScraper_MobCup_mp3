import requests
import re
import os
import urllib.parse
from bs4 import BeautifulSoup as bs

searchword=input("Enter Song to Search\n\n")
new = requests.get("https://mobcup.net/search?q="+urllib.parse.quote(searchword)+"&type=ringtone")
soup = bs(new.content, "html.parser")

for i in soup.find_all('div',class_='item ringtone'):
    subpagelink="https://mobcup.net"+str(i.find('a')['href'])
    subpage=bs(requests.get(subpagelink).content,"html.parser")
    for t in subpage.find_all('a',class_='download-btn'):
        a="https://mobcup.net"+str(t.get('href'))
        if(re.search("mp3",a)):
            song=requests.get(a)
            name=" ".join(a.split("/")[-3].split("-")[:-1]).replace('-',' ')+".mp3"
            with open(os.path.join('T:\Web Scraping\Downloads',name), "wb") as f:
                #add the absolute location of the directory above
                f.write(song.content)
            print("\n"+a+" Done")

print("\nFinished!")
