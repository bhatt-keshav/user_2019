import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
# tells that the request for this web page succeeded by checking the status_code attribute of the Response object. If it is equal to the value of requests.codes.ok, then everything went fine
res.status_code == requests.codes.ok
# if res.status_code == 200, then ok; 404 nok
res.text[:200]

playFile = open('RJ.txt', 'wb')
# This won't work, as a bytes-like object is required, not 'str'
#  but it’s to ensure that the requests module doesn’t eat up too much memory even if you download massive files.
# playFile.write(res.text) 
for chunk in res.iter_content(100000):
    playFile.write(chunk)    
playFile.close()

# For where there is no page (404) #
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc) )

