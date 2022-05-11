from dataclasses import dataclass


@dataclass
class Site:
	url: str
	title: str
	texts: list[str]
	themes: list[str]
