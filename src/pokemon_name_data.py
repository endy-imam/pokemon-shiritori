class PokemonNameData:

	def __init__(self, tup):
		self.dex_number = int(tup[0])
		self.english = tup[1]
		self.japanese = tup[2]
		self.transliterate = tup[3]
		self.romaji = tup[4]

	def __str__(self):
		return f'{self.dex_number:03d}. {self.japanese} ' \
		       f'({self.transliterate} | {self.english})'

	def __repr__(self):
		return f'PokemonNameData({self.dex_number}, {self.english}, ' \
		           f'{self.japanese}, {self.transliterate}, {self.romaji})'
