import bs4 as bs
import urllib.request
from urllib.request import urlopen
import pprint

base_url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePage_false_0&entitySelectingHelper.selectedEntity=d290&zip=97201'
n = 10

i = 5

modified_url = (base_url + '#resultsPage=' + str(i))

print(modified_url)

#soup = bs.BeautifulSoup(modified_url, 'lxml')
#body = soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)
