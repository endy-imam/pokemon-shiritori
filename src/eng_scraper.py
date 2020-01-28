#!/usr/bin/env python
# -*- coding: utf-8 -*-
# English Pokémon Name Scraper

import requests
from bs4 import BeautifulSoup

# Get the HTML
url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html5lib")

# Get the tables
gen_count = 8
table_by_gen = soup.find_all('table')[1:(1+gen_count)]

# Output Table
eng_names = [('NDex', 'English Name', 'Generation')]

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
			eng_names.append((dex_num, name, num))

# output files to CSV
with open('../data/eng_names.csv','w',encoding='utf-8') as out_file:
	out_file.write(', '.join(eng_names[0]) + '\n')
	for entry in eng_names[1:]:
		(num, name, gen) = entry
		out_file.write(f' {num:3d}, {name}, {gen}\n')
