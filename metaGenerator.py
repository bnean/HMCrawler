from urllib.request import urlopen
from urllib.request import urlretrieve
from lxml import etree
import lxml.html
import re
import os
import sqlite3
import time


rootURL = 'http://www2.hm.com'
rootDir='/home/bjarn/Desktop/python-crawler/' #CHANGE TO FIT YOUR ENVIRONMENT
stopWordsPath = rootDir+'stopwords'


db='images.db'
condb = sqlite3.connect(db)
file = open(stopWordsPath, 'r')
stopWordsText = file.read()
file.close()
stopwords = stopWordsText.split(', ')
#print(stopwords)
with condb:
	cursor=condb.cursor()
	cursor.execute("DROP TABLE IF EXISTS Images")
	cursor.execute("CREATE TABLE Images(Id TEXT PRIMARY KEY, Top TEXT, Gender TEXT, Metadata TEXT)")
	for gender in ['men','ladies']:
		for topBottom in ['top','bottom']:
				path = rootDir+'htmlfiles/'+gender+'/'+topBottom+'/'
				filenames = os.listdir(path)
				#should be trivial to implement multithreading
				for filename in filenames:
					file = open(path+filename, 'r')
					htmlFile =  lxml.html.fromstring(file.read())
					file.close()

					for html in htmlFile.xpath("//script[not(@*) and contains(text(), 'var productArticleDetails')]"):
						productInfo = etree.tostring(html, encoding='unicode', pretty_print=True)
						productInfo = " ".join(productInfo.split())

						pids = re.findall ("(?<=')[0-9]{10}(?=': {)", productInfo)
						#print(pids)
						
						color = re.findall ("(?<='name': ')[A-Za-z ]*", productInfo)
						#print(name)

						descFull = re.findall ("(?<='description': ')[^']*", productInfo)
						#print(descFull)
						iterator = 0 
						for descirino in descFull:
							for stopWord in stopwords:
								descirino = descirino.replace(" "+stopWord+" ", " ")
								#print(descirino)
								#print(stopWord)
							descirino = descirino.replace(".", "")
							descirino = descirino.replace(",", "")
							desc =descirino
							iterator += 1
						#print(descSplit)

						images = re.findall("(?<='images':\[ \{ )[^}]*", productInfo)
						iterator = 0
						for image in images:

								
							image = re.findall ("(?<='image': '//)[^']*", image)
							image=image[0].replace("amp;", "").replace(" ", "")
							print('ProdId: '+pids[iterator])
							print('Image: http://'+image)
							print(topBottom)
							print('Meta-data: ', desc)
							time.sleep(.2) #anti-ddos protection :P
							#pids should be in same order as images
							urlretrieve('http://'+image, rootDir+'images/'+pids[iterator]+'.jpg') 
							cursor.execute("INSERT OR IGNORE INTO Images(Id, Top, Gender, Metadata) VALUES('"+pids[iterator]+"','"+topBottom+"','"+gender+"','"+color[iterator]+" "+desc+"')")
							iterator += 1
							#condb.commit()
	cursor.execute("SELECT * FROM Images")
	rows = cursor.fetchall()

	for row in rows:
		print (row)



