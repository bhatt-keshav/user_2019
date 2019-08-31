### Dependencies
import os, re
import bs4, requests
from random import random
import time
import win32com.client

### Initialize
website = 'http://www.user2019.fr'
res = requests.get(website + '/talk_schedule/')
res.status_code == 200
# res.text converts the html that was downloaded by the requests into a txt
# res.text actually contains the entire html 
user19Soup = bs4.BeautifulSoup(res.text)
type(user19Soup)
trFiltered = user19Soup.find_all('tr', class_='filtered')

# Finds out all extensions
exts = []
for tr in trFiltered:
    fileName = tr.a.get('href')
    ex = re.search(r'\..*', fileName).group()
    exts.append(ex)
set(exts)
usualExts = ['.zip', '.pdf', '.pptx', '.html']

# This method returns only the alphabets
def OnlyAlphas(tag):
    tagAlpha = " ".join(re.findall("[a-zA-Z]+", tag.getText()))
    return tagAlpha

# This script fetches everything
for tr in trFiltered:
    t1, t2, t3 = tr.select("td:nth-of-type(3), td:nth-of-type(4), td:nth-of-type(5)")
    tName = OnlyAlphas(t1) + '_' + OnlyAlphas(t2) + '_' + OnlyAlphas(t3)
    fileN = tr.a.get('href')    
    ext = re.search(r'\..*', fileN).group()        
    print('starting to fetch')
    # if exts in usualExts then go ahead, otherwise
    if ext in usualExts:
        resFile = requests.get(website + fileN)
        outFile = open(os.getcwd() + '\\downloads\\' + tName + ext, 'wb')
        resFileIter = resFile
        resFile.close()
        for chunk in resFileIter.iter_content(100000):
            outFile.write(chunk)
        outFile.close()
    else:
        outFileUrl = os.getcwd() + '\\downloads\\' + tName + '.url'
        ws = win32com.client.Dispatch("wscript.shell")
        shortcut = ws.CreateShortcut(outFileUrl)
        shortcut.TargetPath = fileN
        shortcut.Save()
    print('fetched')
    time.sleep(random())
    print('sleeping')
print('done')