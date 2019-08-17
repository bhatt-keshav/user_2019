import bs4, requests
# import os
res = requests.get('http://nostarch.com')
# res.raise_for_status == requests.codes.ok # WHY?
res.status_code == 200
# res.text converts the html that was downloaded by the requests into a txt
# res.text actually contains the entire html 
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

noStarchSoup.select("p:nth-of-type(1)")

# this just opens the file as an IO thing, but does not read the contents as yet
examp = open('ex.html')
# to read the contents, you need to do this
exampText = examp.read() 
# and then pass it to beautiful soup
exampSoup = bs4.BeautifulSoup(exampText)
# exampSoup = bs4.BeautifulSoup(examp.read()), if this is done it will just read the io thing = io.TextIOWrapper name='ex.html' mode='r' encoding='cp1252' and return nothing out
type(exampSoup)
# The exampSoup is separated by bs4
exampSoup
elems = exampSoup.select('#author')
len(elems)
# By doing so we get into the text inside the author element
elems[0].getText()
# Below gives ouput with HTML tags
elems
# Below gives a dictionary format
elems[0].attrs

pElems = exampSoup.select('p')
# the get method gives the attributes of that element, e.g.
pElems[1].get('class')
# while the getText, outputs the inner text stored in the element
pElems[1].getText()

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/tillie" class="sister" id="link3">Millie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = bs4.BeautifulSoup(html_doc, 'html.parser')
soup.select("a:nth-of-type(2)")




