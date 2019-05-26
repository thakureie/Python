'''
import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

'''

import sys, requests, webbrowser, bs4,time

print("Googling Again.......................")
res = requests.get('http://google.com/search?q='  + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
 time.sleep(10)
 webbrowser.open('http://google.com' + linkElems[i].get('href'))

