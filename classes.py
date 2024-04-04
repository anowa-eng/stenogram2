from abc import abstractmethod
from typing import Dict
from cv2.typing import Point, MatLike
from pysle import isletool
from hyphen import Hyphenator

_isle = isletool.Isle()
_hyphenator = Hyphenator()

class PolylinesGlyphPath:
    def __init__(self, points: list[Point]):
        self.points = points
    
class PolylinesGlyph:
    def __init__(self, path: list[PolylinesGlyphPath], joining_point: Point = None):
        self.path = path
        self.joining_point = joining_point or path[-1]

class Shorthand:
    @abstractmethod
    def convert(string: str):
        pass

class WrittenShorthand(Shorthand):
    @property
    @abstractmethod
    def glyphs() -> Dict[str, PolylinesGlyph]:
        pass
    @abstractmethod
    def convert(string: str) -> MatLike:
        pass

class TypableShorthand(Shorthand):
    @abstractmethod
    def convert(string: str) -> str:
        pass

class Word:
    def __init__(self, word: str):
        self.word = word
        self.syllables = _hyphenator.syllables(word)
        self.pronunciations = _isle.lookup(word)
