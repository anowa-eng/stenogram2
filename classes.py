import repackage
repackage.up()

import abc
from typing import Dict, List
from cv2.typing import Point, MatLike
from syllabifier import syllabifier
from nltk.tokenize.sonority_sequencing import SyllableTokenizer

class PolylinesGlyphPath:

	def __init__(self, points: list[Point]):
		self.points = points


class PolylinesGlyph:

	def __init__(self,
	             path: list[PolylinesGlyphPath],
	             joining_point: Point = None):
		self.path = path
		self.joining_point = joining_point or path[-1]


class Word:
	__SSP = SyllableTokenizer()
	def __init__(self, word: str):
		self.word = word
		self.arpabet_syllables = syllabifier.generate(word)
		if self.arpabet_syllables is None:
			raise Exception(f'Could not find "{word}" in CMU Pronouncing Dictionary')
		# TODO: Add Onceler() from eng-syl to split the words.
		self.syllables = self.__SSP.tokenize(word)

# sorry
print(Word('use').arpabet_syllables)

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
