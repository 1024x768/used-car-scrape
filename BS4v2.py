import bs4 as bs
import urllib.request
from urllib.request import urlopen

sauce = urlopen('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePage_false_0&entitySelectingHelper.selectedEntity=d290&zip=97201').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# request page 1 through 10

n = 10
for i in range(1, n+1):
    body = soup.body
    for paragraph in body.find_all('p'):
        print(paragraph.text)
