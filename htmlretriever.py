from urllib.request import urlopen
from urllib.request import urlretrieve
import lxml.html
import re
import time

rootURL = 'http://www2.hm.com'
rootDir='/home/bjarn/Desktop/python-crawler/' #CHANGE TO FIT YOUR ENVIRONMENT

#couldnt find a page showing all products?
urlsTop = ['/en_gb/men/shop-by-product/basics/hoodies-and-sweatshirts.html',
'/en_gb/men/shop-by-product/basics/t-shirts.html',
'/en_gb/men/shop-by-product/blazers-and-suits/blazers.html',
'/en_gb/men/shop-by-product/cardigans-and-jumpers.html',
'/en_gb/men/shop-by-product/hm-sport/jackets.html',
'/en_gb/men/shop-by-product/hm-sport/tops.html',
'/en_gb/men/shop-by-product/hoodies-and-sweatshirts.html',
'/en_gb/men/shop-by-product/jackets-and-coats.html',
'/en_gb/men/shop-by-product/shirts.html',
'/en_gb/men/shop-by-product/t-shirts-and-vests.html',
'/en_gb/ladies/shop-by-product/basics/tops/vests.html',
'/en_gb/ladies/shop-by-product/basics/tops/short-sleeve.html',
'/en_gb/ladies/shop-by-product/basics/tops/long-sleeve.html',
'/en_gb/ladies/shop-by-product/basics/cardigans-and-jumpers.html',
'/en_gb/ladies/shop-by-product/blazers-and-waistcoats/blazers.html',
'/en_gb/ladies/shop-by-product/blazers-and-waistcoats/kimonos.html',
'/en_gb/ladies/shop-by-product/blazers-and-waistcoats/waistcoats.html',
'/en_gb/ladies/shop-by-product/cardigans-and-jumpers/cardigans.html',
'/en_gb/ladies/shop-by-product/cardigans-and-jumpers/hoodies-and-sweatshirts.html',
'/en_gb/ladies/shop-by-product/cardigans-and-jumpers/jumpers.html',
'/en_gb/ladies/shop-by-product/cardigans-and-jumpers/ponchos.html',
'/en_gb/ladies/shop-by-product/cardigans-and-jumpers/turtlenecks.html',
'/en_gb/ladies/shop-by-product/jackets-and-coats/coats.html',
'/en_gb/ladies/shop-by-product/jackets-and-coats/jackets.html',
'/en_gb/ladies/shop-by-product/shirts-and-blouses/blouses.html',
'/en_gb/ladies/shop-by-product/shirts-and-blouses/shirts.html',
'/en_gb/ladies/shop-by-product/shirts-and-blouses/tunics.html',
'/en_gb/ladies/shop-by-product/tops/basics.html',
'/en_gb/ladies/shop-by-product/tops/cropped-tops.html'
'/en_gb/ladies/shop-by-product/tops/long-sleeve.html',
'/en_gb/ladies/shop-by-product/tops/short-sleeve.html',
'/en_gb/ladies/shop-by-product/tops/vests.html']

urlsBottom = ['/en_gb/men/shop-by-product/blazers-and-suits/suit-pants.html',
'/en_gb/men/shop-by-product/hm-sport/bottoms.html',
'/en_gb/men/shop-by-product/jeans.html',
'/en_gb/men/shop-by-product/trousers.html',
'/en_gb/men/shop-by-product/shorts.html',
'/en_gb/ladies/shop-by-product/basics/dresses-and-skirts.html',
'/en_gb/ladies/shop-by-product/basics/trousers-and-leggings.html',
'/en_gb/ladies/shop-by-product/jeans/boyfriend.html',
'/en_gb/ladies/shop-by-product/jeans/flare.html',
'/en_gb/ladies/shop-by-product/jeans/shaping-skinny.html',
'/en_gb/ladies/shop-by-product/jeans/skinny.html',
'/en_gb/ladies/shop-by-product/jeans/super-skinny.html',
'/en_gb/ladies/shop-by-product/jeans/super-skinny-jeggings.html',
'/en_gb/ladies/shop-by-product/shorts/denim-shorts.html',
'/en_gb/ladies/shop-by-product/shorts.html',
'/en_gb/ladies/shop-by-product/skirts/long-skirts.html',
'/en_gb/ladies/shop-by-product/skirts/midi-skirts.html',
'/en_gb/ladies/shop-by-product/skirts/short-skirts.html',
'/en_gb/ladies/shop-by-product/trousers/chinos-slacks.html',
'/en_gb/ladies/shop-by-product/trousers/culottes.html',
'/en_gb/ladies/shop-by-product/trousers/flare.html',
'/en_gb/ladies/shop-by-product/trousers/joggers.html',
'/en_gb/ladies/shop-by-product/trousers/leggings.html',
'/en_gb/ladies/shop-by-product/trousers/slim.html',
'/en_gb/ladies/shop-by-product/trousers/sports-trousers.html']


for url in urlsTop:
    connection = urlopen(rootURL+url)
    htmlFile =  lxml.html.fromstring(connection.read())
    time.sleep(.2) #anti-ddos protection :P
    for link in htmlFile.xpath('//a/@href'): # select the url in href for all a tags(links)

        linkMatch=re.match('/en_gb/productpage.*', link) # only retrieve product links
        if linkMatch:
            menMatch = re.match ('.*men.*', url)
            if menMatch:
                pid = link[19:29]#extract productID. There are more pids hidden inside the html files though
                print(link)
                print(pid)
                urlretrieve(rootURL+link, rootDir+'htmlfiles/men/top/'+pid)
            else:
                pid = link[19:29]#extract productID. There are more pids hidden inside the html files though
                print(link)
                print(pid)
                urlretrieve(rootURL+link, rootDir+'htmlfiles/ladies/top/'+pid)

for url in urlsBottom:
    connection = urlopen(rootURL+url)
    htmlFile =  lxml.html.fromstring(connection.read())
    time.sleep(.2) #anti-ddos protection :P
    for link in htmlFile.xpath('//a/@href'): # select the url in href for all a tags(links)

        linkMatch=re.match('/en_gb/productpage.*', link) # only retrieve product links
        if linkMatch:
            menMatch = re.match ('.*men.*', url)
            if menMatch:
                pid = link[19:29]#extract productID. There are more pids hidden inside the html files though
                print(link)
                print(pid)
                urlretrieve(rootURL+link, rootDir+'htmlfiles/men/bottom/'+pid)
            else:
                pid = link[19:29]#extract productID. There are more pids hidden inside the html files though
                print(link)
                print(pid)
                urlretrieve(rootURL+link, rootDir+'htmlfiles/ladies/bottom/'+pid)