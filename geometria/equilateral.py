from .triangle import Triangle
import math

class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_equilateral(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return math.isclose(ab, bc) and math.isclose(bc, ca)
