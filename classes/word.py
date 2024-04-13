from ..syllabifier import syllabifier
from nltk.tokenize.sonority_sequencing import SyllableTokenizer
from eng_syl.onceler import Onceler

class Syllable:
	def __init__(self, onset_nucleus_coda_list: list[str]):
		onset, nucleus, coda = [None, None, None]
		print(onset_nucleus_coda_list)
		match len(onset_nucleus_coda_list):
			case 2:
				nucleus, coda = onset_nucleus_coda_list
			case 3:
				onset, nucleus, coda = onset_nucleus_coda_list
			case _:
				raise ValueError(f"Cannot separate syllable with {len(onset_nucleus_coda_list)} parts")
		self.onset = None if onset == '' else onset
		self.nucleus = None if nucleus == '' else nucleus
		self.coda =  None if coda == '' else coda
	def __repr__(self):
		return f"Syllable(onset={self.onset}, nucleus={self.nucleus}, coda={self.coda})"

class Word:
	__SSP = SyllableTokenizer()
	__onceler = Onceler()
	def __init__(self, word: str):
		self.word = word
		self.arpabet_syllables = syllabifier.generate(word)
		if self.arpabet_syllables is None:
			raise Exception(f'Could not find "{word}" in CMU Pronouncing Dictionary')
		# TODO: Improve accuracy
		ssp_syllables = self.__SSP.tokenize(word)
		print(ssp_syllables)
		syllables = [Syllable(self.__onceler.onc_split(i).split('-')) for i in ssp_syllables]
		self.syllables = zip(syllables, self.arpabet_syllables)