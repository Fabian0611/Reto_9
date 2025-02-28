import time
from geometria.point import Point
from geometria.line import Line

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} {end_time - start_time:.6f} seconds")
        return result
    return wrapper

class Shape:
    _shape_type = "Any Shape"

    def __init__(self, vertices):
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError("Vertices must be instances of Point.")  # verifica que el argumento sea un objeto Point
        self._vertices = vertices
        self._edges = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges
    
    @property
    def shape_type(self):
        return self._shape_type

    @timing_decorator
    def compute_area(self):
        ...

    def compute_perimeter(self):
        return sum(edge.length() for edge in self._edges)

    @classmethod
    def set_shape_type(cls, new_type):
        if cls == Shape:  # Solo permite cambiar el tipo de Shape, no de subclases
            cls._shape_type = new_type

