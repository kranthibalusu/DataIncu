from bs4 import BeautifulSoup as BS
import urllib.request
import csv
import re


file = open('episodes.txt','r')
episodes=file.readlines() 
file.close()




charLinesData = {}
#line number 
idNo = 0
scene = 0

with open('data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter='|',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #loop through each episode webpage
    for episode in episodes:
        episode= episode.strip()

        #open episode html 
        if len(episode)<5:
            address = 'https://fangj.github.io/friends/season/0'+episode+'.html'
        else:
            address = 'https://fangj.github.io/friends/season/'+episode+'.html'
        print(address)
        episodeNo = episode[-2:]
        seas = episode[:-2]
        print(episodeNo)
        print(seas)
        html = urllib.request.urlopen(address)
        soup = BS(html, 'html.parser')
        lines=soup.find_all('b')
    
        for line in lines:
            idNo = idNo + 1
            row=[]
            charecter =line.get_text()
            charecter = charecter[0:-1]
            #print(type(charecter))
            charLine = line.next_sibling
            #charLine=charLine.get_text()
            if charLine is not None:
                if '[Scene:' in charLine:
                    scene = scene + 1
                else:
                    charLine.strip()
                    #words = charLine.split()
                    re.sub('[^a-zA-Z0-9-_*.]', '', charLine)
                    #print(charLine)
                    row = [str(idNo), seas, episodeNo, scene , charLine, charecter]
                    print(type(charLine))
                    filewriter.writerow(row)
                

csvfile.close()
    
        

    

