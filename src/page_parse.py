import requests
from bs4 import BeautifulSoup

url = "https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)#Name_origin"


class NameObject:

	def __init__(self, raw, alt=None):
		self.raw = raw
		self.alt = alt

	def __str__(self):
		if self.alt is None:
			return self.raw
		else:
			return f'{self.raw} ({self.alt})'

	def __repr__(self):
		return f'NameObject({self.raw}, {self.alt})'


def language_parse (url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")

	big_tags = soup.find_all('big')
	language_table = soup.find(string='Language').find_parent('table')
	language_entries = language_table.find_all('tr')[1:-1]

	eng_name = big_tags[0].text

	language_list = {'English': NameObject(eng_name, None)}
	for entry in language_entries:
		td = entry.find_all('td')
		lang = td[0].text.strip()
		name = td[1].text.split()[0]
		litr = td[1].i
		if litr is not None:
			litr = litr.text
		language_list[lang] = NameObject(name, litr)

	return language_list

"""
class PokemonPageData:

	def __init__(self, url):
		response = requests.get(url)
		soup = BeautifulSoup(response.text, "lxml")

		self.names
"""

for key, val in language_parse(url).items():
	out_val = f'"{val.raw}"'
	if val.alt is not None:
		out_val = f'["{val.raw}", "{val.alt}"]'
	print(f'"{key}": {out_val}')
