#!/usr/bin/env python
# -*- coding: utf-8 -*-
# English Pokémon Name Scraper

import csv
import requests
from bs4 import BeautifulSoup

# Get the HTML
parent_url = 'https://bulbapedia.bulbagarden.net'
url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Get the tables
gen_count = 8
table_by_gen = soup.find_all('table')[1:(1+gen_count)]

# Output Table
names = [('NDex', 'English', 'Japanese', 'Romaji', 'Translit')]


# japanese name data
def jpn_parse (url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")
	soup = soup.find(string='Catch rate').find_parent('table')
	soup = soup.tr.table.tr.find_all('td')[2]

	jpn = soup.b.text
	translit = soup.i.text
	romaji = soup.b.span
	if romaji is not None:
		romaji = romaji['title']
	else:
		romaji = translit

	return (jpn, romaji, translit)


# get the table for each generation
prev_num = 0
for (num, region_table) in enumerate(table_by_gen, 1):
	region_entries = region_table.find_all('tr')[1:]

	# get the entry for each region
	for entry in region_entries:
		td = entry.find_all('td')
		dex_num = td[1].text.strip()[1:]
		# prevent same numbering and question marks
		if dex_num != '???' and prev_num != int(dex_num):
			dex_num = int(dex_num)
			prev_num = dex_num
			name = td[2].text.strip()
			# Get Japanese Names from Link
			new_url = parent_url + td[2].a['href']
			print(f'Looking at #{dex_num:03d}: {name}')
			(jpn, translit, romaji) = jpn_parse(new_url)

			names.append((dex_num, name, jpn, translit, romaji))

# output files to CSV
with open('../data/names.csv','w',encoding='utf-8') as out_file:
	writer = csv.writer(out_file,lineterminator='\n')
	writer.writerows(names)
