from collections import namedtuple
import repackage
repackage.up()

import abc
from typing import Dict, List
from cv2.typing import Point, MatLike
from syllabifier import syllabifier
from nltk.tokenize.sonority_sequencing import SyllableTokenizer
from eng_syl.onceler import Onceler
from collections import namedtuple

class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

class PolylinesGlyphPath:

	def __init__(self, points: list[Point]):
		self.points = points


class PolylinesGlyph:

	def __init__(self,
	             path: list[PolylinesGlyphPath],
	             joining_point: Point = None):
		self.path = path
		self.joining_point = joining_point or path[-1]

class Syllable:
	def __init__(self, onset_nucleus_coda_list: list[str]):
		onset, nucleus, coda = [None, None, None]
		match len(onset_nucleus_coda_list):
			case 2:
				nucleus, coda = onset_nucleus_coda_list
			case 3:
				onset, nucleus, coda = onset_nucleus_coda_list
			case _:
				raise ValueError(f"Cannot separate syllable with {len(onset_nucleus_coda_list)} parts")
		self.onset = None if onset == '' else onset
		self.nucleus = None if nucleus == '' else nucleus
		self.coda =  None if coda == '' else onset
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
		syllables = [Syllable(self.__onceler.onc_split(i).split('-')) for i in ssp_syllables]
		self.syllables = zip(syllables, self.arpabet_syllables)

# sorry
print(list(Word('colonel').syllables))

class Shorthand(abc.ABC):

	@staticmethod
	@abc.abstractmethod
	def briefs() -> Dict[str, List[str]]:
		pass

	@staticmethod
	@abc.abstractmethod
	def build_word(
	    word: Word):  # Adjusted parameter type to be a superclass of Shorthand
		pass

	@staticmethod
	@abc.abstractmethod
	def convert(string: str):
		pass


class WrittenShorthand(Shorthand):

	@staticmethod
	@abc.abstractmethod
	def glyphs() -> Dict[str, PolylinesGlyph]:
		pass

	@staticmethod
	@abc.abstractmethod
	def convert(string: str) -> MatLike:
		pass
