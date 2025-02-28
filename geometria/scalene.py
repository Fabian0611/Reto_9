from .triangle import Triangle
import math

class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_scalene(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return not (math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab))
