import bs4 as bs
import urllib.request
from urllib.request import urlopen
import time
base_url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePage_false_0&entitySelectingHelper.selectedEntity=d290&zip=97201'

n=10

for i in range(1, n+1):    
    print('\n \n THIS IS THE ' + str(i) + ' ITERATION OF THIS REQUEST \n \n')
    modified_url = urlopen(base_url + '#resultsPage=' + str(i)).read()
    
    soup = bs.BeautifulSoup(modified_url, 'lxml')
    body = soup.body
    for paragraph in body.find_all('p'):
        print(paragraph.text)
    time.sleep(5)
