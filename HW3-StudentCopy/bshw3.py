# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import requests
import re
from bs4 import BeautifulSoup

fopen = open('index.html', 'w')

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')


student_text = soup.find_all(text=re.compile('student'))
for line in student_text:
	#if re.search('student', line):
	text_sub = line.replace('student', 'AMAZING student')
	#print (text_sub)
	line.replace_with(text_sub)

for img in soup.find_all('img'):
	if	img['src'] == 'logo2.png':
		img['src'] = 'media/logo.png'
	else:
		img['src'] = 'media/owen.png'

prettify = soup.prettify()
fopen.write(prettify)			
	

