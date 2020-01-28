#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Japanese Pokémon Name Scraper

import requests
from bs4 import BeautifulSoup

# Get the HTML
url = 'https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E4%B8%80%E8%A6%A7'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html5lib")

# Output File
jpn_names = [('NDex', 'Japanese Kana')]

# Get the tables
full_table = soup.find('table')
entries = full_table.find_all('tr')[1:]

# get the entry for the entire list
prev_num = 0
for entry in entries:
	td = entry.find_all('td')
	num = td[0].text.strip()
	name = td[1].text.strip().split('(')[0]
	if num != '' and prev_num != int(num):
		num = int(num)
		prev_num = num
		jpn_names.append((num, name))

# output files to CSV
with open('../data/jpn_names.csv','w',encoding='utf-8') as out_file:
	out_file.write(', '.join(jpn_names[0]) + '\n')
	for entry in jpn_names[1:]:
		(num, name) = entry
		out_file.write(f' {num:3d}, {name}\n')
