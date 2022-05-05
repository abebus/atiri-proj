from dataclasses import dataclass
import requests as req
import bs4 as bs


@dataclass
class Site:
	url: str
	title: str
	texts: list[str]
	themes: list[str]


def parser():
	sites = [site.strip() for site in open('sites.txt')]
	for site in sites:
		soup = bs.BeautifulSoup(req.get(url=site).text, 'lxml')
		title = soup.find_all('title')[0].get_text().strip()
		search_list = ['keywords', 'description', 'Keywords', 'Description']
		text = []
		for val in search_list:
			for meta in soup.find_all('meta', attrs={'name': val}):
				text.append(meta['content'].strip())
		a = Site(url=site, title=title, texts=text)
		print(a)
	
	
def analyser():
	pass
