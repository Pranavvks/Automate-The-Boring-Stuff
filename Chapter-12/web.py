#!python3
from bs4 import BeautifulSoup
import requests as rq 
import os

r = rq.get('https://www.pexels.com/@rb-retratos')
soup=BeautifulSoup(r2.text,"html.parser")

links=[]

x=soup2.select('img[src^="https://images.pexels.com/photos"]')

for img in x:
    links.append(img['src'])

os.mkdir('pexels_phots')
i= 1
for index , img_link in enumerate (links):
    if i<=5:
        img_data=rq.get(img_link).content
        with open ("pexels_photos/"+str(index+1)+'.png','wb') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break

