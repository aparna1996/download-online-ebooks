import os, requests, bs4, re
url = 'http://www.freevampires.net/young/yd4302.html' #write the parent url here

#os.makedirs('mitosis', exist_ok=True) #write the folder name here
num = 9 #total number of pages 

r = requests.get(url) #download the first page
r. raise_for_status()
text = bs4.BeautifulSoup(r.text, "lxml")
page2 = text.select('.text')

page2 = str(page2)
page = re.sub('<.*?>','',page2) #removes html content from it

f = open('file.txt', 'w')
f.write(page)

for s in range(2, num+1):
	url2 = url.replace('.html','_'+str(s)+'.html')
	r = requests.get(url2) 
	r. raise_for_status()
	text = bs4.BeautifulSoup(r.text, "lxml")
	page2 = text.select('.text')
	page2 = str(page2)	
	page = re.sub('<.*?>','',page2) #removes html content from it
	f = open('file.txt', 'a')
	f.write(page)

f.close()
