import requests as req
from bs4 import BeautifulSoup


def parser(site: str, tag: str = None) -> str:
	"""
	Вернуть весь текст и метаданные сайта, содержащие его описание и ключевые слова
	
	:param site: url сайта
	:param tag: уточнение возвращаемых данных
		если tag='body', то возвращается весь текст сайта.
	    если 'meta'- только описание и ключевые слова
	    если 'both' экв. tag is None- возврат и метаданных и основного текста сайта
	:return str: текст сайта / что было в метатеге
	"""
	
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
	for script in soup(["script", "style"]):  # не учитываем содержание скриптов и css
		script.extract()
	
	if tag == 'meta':
		return get_kwds_and_desc(soup)
	elif tag == 'body':
		return get_plain_text(soup)
	elif tag == 'both' or not tag:
		return get_kwds_and_desc(soup) + '\n\n' + get_plain_text(soup)
