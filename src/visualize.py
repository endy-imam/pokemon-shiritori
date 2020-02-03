# Visualization

import math
import csv
import networkx as nx
import matplotlib.pyplot as plt
from shiritori_parse import shiritori_parse
from pokemon_name_data import PokemonNameData


def parse_csv():
	with open('../data/names.csv','r',encoding='utf-8') as in_file:
		reader = csv.reader(in_file)
		next(reader)
		return [PokemonNameData(row) for row in reader]

def color_input(val):
	return str(math.pow(1 - val, .9))


entries = parse_csv()

kanas = set()
edges = {}
max_weight = 0
for entry in entries:
	(first, last) = shiritori_parse(entry.japanese)
	kanas = kanas | {first, last}
	if (first, last) in edges.keys():
		edges[(first, last)] = edges[(first, last)] + 1
	else:
		edges[(first, last)] = 1

	if edges[(first, last)] > max_weight:
		max_weight = edges[(first, last)]

kanas = sorted(kanas)

edges = {k: v for k, v in sorted(edges.items(), key=lambda item: item[1])}
edge_colors = [color_input(val / max_weight) for val in edges.values()]

edges = [key for key in edges.keys()]


G = nx.DiGraph()
G.add_nodes_from(kanas)
G.add_edges_from(edges)

nx.draw_circular(G, with_labels=True, edge_color=edge_colors, width=0.75)
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "MS Gothic"
plt.show()
