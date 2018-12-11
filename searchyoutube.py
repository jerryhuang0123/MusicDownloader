import urllib.request
from bs4 import BeautifulSoup

def SearchYoutube(textToSearch):
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	return 'https://www.youtube.com' + soup.find(attrs={'class':'yt-uix-tile-link'})['href']
	#return soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	#    arr.append('https://www.youtube.com' + vid['href'])
	#return arr