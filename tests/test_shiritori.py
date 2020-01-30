import unittest
from src.shiritori_parse import shiritori_parse

class TestShiritori(unittest.TestCase):

	def test_shiritori(self):
		# Pikachu, Klefki, Starmie, Snivy
		self.assertEqual(shiritori_parse('ピカチュウ'), ('ピ', 'ウ'))
		self.assertEqual(shiritori_parse('クレッフィ'), ('ク', 'イ'))
		self.assertEqual(shiritori_parse('スターミー'), ('ス', 'ミ'))
		self.assertEqual(shiritori_parse('ツタージャ'), ('ツ', 'ヤ'))

	def test_shiritori_outlier(self):
		# Nidorans (Male + Female), Porygon 2/Z
		self.assertEqual(shiritori_parse('ニドラン♂'), ('ニ', 'ン'))
		self.assertEqual(shiritori_parse('ニドラン♀'), ('ニ', 'ン'))
		self.assertEqual(shiritori_parse('ポリゴン2'), ('ポ', 'ツ'))
		self.assertEqual(shiritori_parse('ポリゴンZ'), ('ポ', 'ド'))


if __name__ == '__main__':
	unittest.main(verbosity=2)
