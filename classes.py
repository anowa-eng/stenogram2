import abc
from typing import Dict, Generator, List, Tuple, Optional
from cv2.typing import Point, MatLike
from pysle import isletool
from pyphen import Pyphen
import helpers

_isle = isletool.Isle()

class PolylinesGlyphPath:
    def __init__(self, points: list[Point]):
        self.points = points
    
class PolylinesGlyph:
    def __init__(self, path: list[PolylinesGlyphPath], joining_point: Point = None):
        self.path = path
        self.joining_point = joining_point or path[-1]

class Word:
    def __init__(self, word: str, language: Optional[str] = None):
        self.__pyphen = Pyphen(lang=language)
        self.word = word
        self.__syllables = self.__pyphen.inserted(word, '/').split('/')
        print(self.__syllables)
        self.pronunciations = [i.toList()[0] for i in _isle.lookup(word)]
    def syllables(self, pronunciation: int = 0):
        ipa = self.pronunciations[pronunciation]
        syllables = zip(self.__syllables, ipa)
        for syllable in syllables:
            yield syllable

for s in Word("project", "en-US").syllables(2):
    print(s)

class Shorthand(abc.ABC):
    @property
    @abc.abstractmethod
    def briefs() -> Dict[str, List[str]]:
        pass
    @abc.abstractmethod
    def build_word(word: Word):
        pass
    @abc.abstractmethod
    def convert(string: str):
        pass

class WrittenShorthand(Shorthand):
    @property
    @abc.abstractmethod
    def glyphs() -> Dict[str, PolylinesGlyph]:
        pass
    @abc.abstractmethod
    def convert(string: str) -> MatLike:
        pass
