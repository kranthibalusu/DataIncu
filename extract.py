from bs4 import BeautifulSoup as BS
import urllib.request 

file = open('episodes.txt','r')
episodes=file.readlines() 
file.close()


f= open("lines.txt","w+")

for episode in episodes[0:2]:
    episode= episode.strip()
    print(episode)
    if len(episode)<5:
        address = 'https://fangj.github.io/friends/season/0'+episode+'.html'
    else:
        address = 'https://fangj.github.io/friends/season/'+episode+'.html'

    print(address)
        
    html = urllib.request.urlopen(address)
    soup = BS(html, 'html.parser')
    tag = soup.a
    tag =tag.get_text()
    f.write(tag+"\n")


f.close()
    
        

    

