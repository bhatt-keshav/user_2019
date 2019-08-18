import bs4, requests, os, re
from random import random
import time
import win32com.client

website = 'http://www.user2019.fr'
res = requests.get(website + '/talk_schedule/')
res.status_code == 200
# res.text converts the html that was downloaded by the requests into a txt
# res.text actually contains the entire html 
user19Soup = bs4.BeautifulSoup(res.text)
type(user19Soup)

trFiltered = user19Soup.find_all('tr', class_='filtered')
# temp jugaad: delete
trFiltered = trFiltered[1:203]
# def chunks(l, n):
#     """Yield successive n-sized chunks from l."""
#     for i in range(0, len(l), n):
#         yield l[i:i + n]

# trFilteredTest = list(chunks(trFiltered, 4))
# len(trFiltered)
# len(trFilteredTest)
# type(trFilteredTest)

# names = []

# for i in range(0, len(trFilteredTest)):
#     for tr in trFiltered[i]:    
#         t1, t2, t3 = tr.select("td:nth-of-type(3), td:nth-of-type(4), td:nth-of-type(5)")
#         t3Alphs = " ".join(re.findall("[a-zA-Z]+", t3.getText()))
#         tName = t1.getText() + '_' + t2.getText() + '_' + t3Alphs
#         fileN = tr.a.get('href')
#         ext = re.search(r'\..*', fileN).group()
#         print('starting to fetch')
#         resFile = requests.get(website + fileN)
#         resFileIter = resFile
#         resFile.close()
#         outFile = open(os.getcwd() + '\\' + tName + ext, 'wb')
#         for chunk in resFileIter.iter_content(1000):
#             outFile.write(chunk)
#     outFile.close()
# print('done')
names = []
exts = []
set(exts)
usualExts = ['.zip', '.pdf', '.pptx', '.html']
for tr in trFiltered:
    t1, t2, t3 = tr.select("td:nth-of-type(3), td:nth-of-type(4), td:nth-of-type(5)")
    t3Alphs = " ".join(re.findall("[a-zA-Z]+", t3.getText()))
    tName = t1.getText() + '_' + t2.getText() + '_' + t3Alphs
    fileN = tr.a.get('href')
    names.append(fileN)    
    ext = re.search(r'\..*', fileN).group()
    exts.append(ext)
    # if exts in ... then go ahead, otherwise skip
    print('starting to fetch')
    resFile = requests.get(website + fileN)
    resFileIter = resFile
    resFile.close()
    outFile = open(os.getcwd() + '\\' + tName + ext, 'wb')
    for chunk in resFileIter.iter_content(1000):
        outFile.write(chunk)
    outFile.close()
    print('sleeping')
    time.sleep(random() * 60)
print('done')
  

# standard case
tr1 = trFiltered[3]
tr1Ext =  re.search(r'\..*', tr1.a.get('href')).group()
tr1Ext in usualExts
# check why nr 4 is not working
tr = trFiltered[5]
t1, t2, t3 = tr.select("td:nth-of-type(3), td:nth-of-type(4), td:nth-of-type(5)")
t3Alphs = " ".join(re.findall("[a-zA-Z]+", t3.getText()))
tName = t1.getText() + '_' + t2.getText() + '_' + t3Alphs
fileN = tr.a.get('href')
ext = re.search(r'\..*', fileN).group()
if ext in usualExts:
    resFile = requests.get(website + fileN)
    outFile = open(os.getcwd() + '\\' + tName + ext, 'wb')
    resFileIter = resFile
    resFile.close()
    for chunk in resFileIter.iter_content(100000):
        outFile.write(chunk)
    outFile.close()
else:
    
   
urlPath = os.getcwd() + '\\' + tName + '.url'
fileN #target
# target = 'http://www.google.com/'
ws = win32com.client.Dispatch("wscript.shell")
shortcut = ws.CreateShortcut(urlPath)
shortcut.TargetPath = fileN
shortcut.Save()


re.search('^\w+.*',tName)
" ".join(re.findall("[a-zA-Z]+", tName))

