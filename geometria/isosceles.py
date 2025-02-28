from .triangle import Triangle
import math

class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_isosceles(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab)
