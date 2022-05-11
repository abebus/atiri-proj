import requests as req
from bs4 import BeautifulSoup


def parser(site, tag=None):
	'''если tag='body', то возвращается весь текст сайта.
	 если 'meta'- только описание и ключевые слова
	 если 'both' экв. tag is None- что делает- понятно'''

	def get_kwds_and_desc(soup):
		search_list = ['keywords', 'description', 'Keywords', 'Description']
		text = ''
		for val in search_list:
			for meta in soup.find_all('meta', attrs={'name': val}):
				text += (meta['content'].strip())
		return text

	def get_plain_text(soup):
		text = soup.get_text().strip()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)
		return text

	soup = BeautifulSoup(req.get(url=site).text, "lxml")
	for script in soup(["script", "style"]): # очистка скриптов и css
		script.extract()

	if tag == 'meta':
		return get_kwds_and_desc(soup)
	elif tag == 'body':
		return get_plain_text(soup)
	elif tag == 'both' or not tag:
		return get_kwds_and_desc(soup) +'\n\n'+ get_plain_text(soup)


if __name__ == '__main__':
	#f = list(open('sites.txt', encoding='utf-8'))[1]
	#print(parser('https://metanit.com/python/tutorial/', 'meta'))
	pass

