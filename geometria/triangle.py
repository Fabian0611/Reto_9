import time
from .shape import Shape

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


class Triangle(Shape):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.")  # verifica que haya exactamente 3 vértices
        super().__init__(vertices)

    @timing_decorator
    def compute_area(self):
        a, b, c = self._vertices
        return abs(a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2

    @property
    def triangle_type(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        if ab + bc <= ca or bc + ca <= ab or ca + ab <= bc:
            raise ValueError("The vertices do not form a valid triangle.")  # verifica si es un triángulo válido
        return ab, bc, ca
