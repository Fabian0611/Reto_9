from .triangle import Triangle
import math

class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)

    def is_right_triangle(self):
        a, b, c = self._vertices
        sides = [a.compute_distance(b), b.compute_distance(c), c.compute_distance(a)]
        sides.sort()
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
