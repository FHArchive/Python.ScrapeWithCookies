'''
Kieran W 2019

Web scraper with cookies. Take the cookie from one page and use it to access
another
'''
# Run the program in 'debug' mode
DEBUG = True
# Web page to scrape
START_PAGE = ''
# Web page to submit answer to
END_PAGE = ''

'''
Start web session and get the cookie
'''
import requests
session = requests.Session()
startPage = session.get(START_PAGE)

pageContents = startPage.text
cookie = session.cookies.get_dict()
if(DEBUG):
	print(pageContents)
	print(cookie)


'''
Scrape the page
'''
from html.parser import HTMLParser
usefulData = []
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if(DEBUG):
			print("<>:", tag)
	def handle_endtag(self, tag):
		if(DEBUG):
			print("</>:", tag)

	def handle_data(self, data):
		if(DEBUG):
			print("Data:", data)
		usefulData.append(data)
parser = MyHTMLParser()
parser.feed(str(pageContents))

if(DEBUG):
	print(usefulData)

'''
Post to another url and pass the cookie
'''
endPage = requests.post(END_PAGE, cookies=cookie)
if(DEBUG):
	print(endPage.text)
