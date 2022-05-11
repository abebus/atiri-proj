import requests as req
from bs4 import BeautifulSoup


def parser(site, tag=None):
	'''если tag=none, то возвращается весь текст сайта.
	 если 'meta'- только описание и ключевые слова
	 если both- понятно'''

	def get_kwds_and_desc(soup):
		search_list = ['keywords', 'description', 'Keywords', 'Description']
		text = ''
		for val in search_list:
			for meta in soup.find_all('meta', attrs={'name': val}):
				text += (meta['content'].strip())
				
		text += '\n\n' + soup.find_all('title')[0].get_text()
		return text
	
	def get_plain_text(soup):
		text = soup.get_text().strip()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)
		return text
	
	soup = BeautifulSoup(req.get(url=site).text, "lxml")
	for script in soup(["script", "style"]):
		script.extract()
		
	if tag == 'meta':
		return get_kwds_and_desc(soup)
	elif tag == 'body':
		return get_plain_text(soup)
	elif tag == 'both' or not tag:
		return get_kwds_and_desc(soup) +'\n\n'+ get_plain_text(soup)


def test():
	f = list(open('sites.txt', encoding='utf-8'))[1]
	print(parser('https://metanit.com/python/tutorial/', 'both'))
