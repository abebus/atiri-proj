import requests as req
from bs4 import BeautifulSoup


def parser(site):
	soup = BeautifulSoup(req.get(url=site).text, "lxml")
	for script in soup(["script", "style"]):
		script.extract()
	text = soup.get_text().strip()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	return text
