import downloader
from urllib.parse import urlparse 
from bs4 import BeautifulSoup as BS
import requests
def main (url):
	if urlparse (url).netloc == "www.newgrounds.com":
		name = BS (requests.get (url).content, "html.parser").find_all ("div", {"class" : "pod-head", "id" : "embed_header"})[0].find ("h2").string
		print (name)
		downloader.main (url = url, gameName = name)
	else:
		print ("Its recomended to use newgrounds")
		downloader.main (url = url, gameName = input ("Game name: "))

if __name__ == "__main__":
	main (input ("Url of the page: "))
	