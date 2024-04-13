from cv2.typing import Point

class PolylinesGlyphPath:

	def __init__(self, points: list[Point]):
		self.points = points


class PolylinesGlyph:

	def __init__(self,
	             path: list[PolylinesGlyphPath],
	             joining_point: Point = None):
		self.path = path
		self.joining_point = joining_point or path[-1]
