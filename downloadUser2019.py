import bs4, requests, os, re

website = 'http://www.user2019.fr'
res = requests.get(website + '/talk_schedule/')
res.status_code == 200
# res.text converts the html that was downloaded by the requests into a txt
# res.text actually contains the entire html 
user19Soup = bs4.BeautifulSoup(res.text)
type(user19Soup)

# to test
names = []
pdfs = []
pdfsUrl = []

trFiltered = user19Soup.find_all('tr', class_='filtered')
trFilteredTest = trFiltered[7:12]

for tr in trFilteredTest:
    t1, t2, t3 = tr.select("td:nth-of-type(3), td:nth-of-type(4), td:nth-of-type(5)")
    t3Alphs = " ".join(re.findall("[a-zA-Z]+", t3.getText()))
    tName = t1.getText() + '_' + t2.getText() + '_' + t3Alphs
    fileN = tr.a.get('href')
    ext = re.search('\..*', fileN).group()
    resFile = requests.get(website + fileN)
    outFile = open(os.getcwd() + '\\' + tName + ext, 'wb')
    for chunk in resFile.iter_content(100000):
        outFile.write(chunk)
    outFile.close()
print('done')
  
# pilot example to put in for loop
fileN = trFiltered[2].a.get('href')
ext = re.search('\..*', fileN).group()
resFile = requests.get(website + fileN)
outFile = open(os.getcwd() + '\\' + 'test' + ext, 'wb')
for chunk in resFile.iter_content(100000):
    outFile.write(chunk)
outFile.close()

# check why hannah is not working
tr = trFiltered[9]
t1, t2, t3 = tr.select("td:nth-of-type(3), td:nth-of-type(4), td:nth-of-type(5)")
t3Alphs = " ".join(re.findall("[a-zA-Z]+", t3.getText()))
tName = t1.getText() + '_' + t2.getText() + '_' + t3Alphs
fileN = tr.a.get('href')
ext = re.search('\..*', fileN).group()
resFile = requests.get(website + fileN)
outFile = open(os.getcwd() + '\\' + tName + ext, 'wb')
for chunk in resFile.iter_content(100000):
    outFile.write(chunk)
outFile.close()

re.search('^\w+.*',tName)
" ".join(re.findall("[a-zA-Z]+", tName))


# TRY
# need 4, 5, 8
a1, a2 = trFiltered[1].select("td:nth-of-type(4), td:nth-of-type(5)")
type(a1.text) #str, but cannot concatenate, still in tag class
type(a1.getText()) #str good
a3 = a1.getText() + '_' + a2.getText()
a = []
a.append(a3)
a.append(a1)
