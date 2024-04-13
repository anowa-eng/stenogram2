import abc
from typing import Dict, List
from cv2.typing import MatLike
from .word import Word
from .glyph import PolylinesGlyph


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
