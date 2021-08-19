import re
from requests import *
from re import *
import xml.etree.ElementTree as ET
from pathlib import *


url = 'https://www.w3schools.com/xml/cd_catalog.xml'


def stream_download(source_url, dest_file):
	r = get(source_url, stream=True)
	dest_file = Path(dest_file)
	with open(dest_file, "wb") as f:
		for chunk in r.iter_content(chunk_size=8192):
			if chunk:
				f.write(chunk)

stream_download(source_url=url, dest_file="cd_catalog.xml")

tree=ET.parse('cd_catalog.xml')

root=tree.getroot()

print("\n Question 2) Il y'a en tout "+str(len(root.getchildren()))+' CD  \n')

for i in range(len(root.getchildren())):
	print('Info sur le CD Numero'+str(i+1))
	print('Titre : '+str(root[i][0].text))
	print('Artiste : '+str(root[i][1].text))
	print('Pays : '+str(root[i][2].text))
	print('Compagnie : '+str(root[i][3].text))
	print('Annee : '+str(root[i][5].text))
	print('\n')


annees=['1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',]
index=[]

for i in range(len(root.getchildren())):
	a=root[i][5].text
	for year in annees:
		if a==year:
			index.append(i)



print("\n Question 3) Il y'a "+str(len(index))+' CD des annees 80 \n')
for i in index:
	
	print('Titre : '+str(root[i][0].text))
	print('Artiste : '+str(root[i][1].text))
	print('Pays : '+str(root[i][2].text))
	print('Compagnie : '+str(root[i][3].text))
	print('Annee : '+str(root[i][5].text))
	print('\n')



pays='UK'
index_langue=[]

for i in range(len(root.getchildren())):
	p=root[i][2].text
	if p==pays:
		index_langue.append(i)


print("\n Question 4) Il y'a "+str(len(index_langue))+' CD anglais (UK) \n')

for i in index_langue:
	
	print('Titre : '+str(root[i][0].text))
	print('Artiste : '+str(root[i][1].text))
	print('Pays : '+str(root[i][2].text))
	print('Compagnie : '+str(root[i][3].text))
	print('Annee : '+str(root[i][5].text))
	print('\n')



