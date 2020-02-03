# Pokemon Shiritori Parse

_char_stepback = { 'ー', '♀', '♂' }
_char_refactor = {
	'ァ': 'ア', 'ィ': 'イ', 'ゥ': 'ウ', 'ェ': 'エ', 'ォ': 'オ',
	'ャ': 'ヤ', 'ュ': 'ユ', 'ョ': 'ヨ',
	'２': 'ツ', '2': 'ツ', 'Z': 'ド'
}

def shiritori_parse(jpn_name):
	"""
	return start and end kana of the given name
	"""
	start = jpn_name[0]
	end = jpn_name[-1]
	if end in _char_stepback:
		end = jpn_name[-2]
	if end in _char_refactor:
		end = _char_refactor[end]
	return (start, end)
