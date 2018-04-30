from bs4 import BeautifulSoup as BS
import urllib.request 

file = open('episodes.txt','r')
episodes=file.readlines() 
file.close()


f= open("lines.txt","w+")


charLinesData = {}


for episode in episodes:
    episode= episode.strip()
    print(episode)
    if len(episode)<5:
        address = 'https://fangj.github.io/friends/season/0'+episode+'.html'
    else:
        address = 'https://fangj.github.io/friends/season/'+episode+'.html'

    print(address)
        
    html = urllib.request.urlopen(address)
    soup = BS(html, 'html.parser')
    lines=soup.find_all('b')
    for line in lines:
        charecter =line.get_text()
        charecter = charecter[0:-1]
        charLine = line.next_sibling
        f.write(charecter +":")
        if charLine is not None:
            f.write(charLine + '\n')
  

f.close()
    
        

    

