import time
from .shape import Shape
from .point import Point

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


class Rectangle(Shape):
    def __init__(self, bottom_left, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric values.")  # verifica que los números dados sean numéricos
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.")  # verifica que los números sean positivos
        vertices = [
            bottom_left,
            Point(bottom_left.x + width, bottom_left.y),
            Point(bottom_left.x + width, bottom_left.y + height),
            Point(bottom_left.x, bottom_left.y + height)
        ]
        super().__init__(vertices)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a numeric value.")  # verifica que el número sea numérico
        if value <= 0:
            raise ValueError("Width must be positive.")  # verifica que el número sea positivo
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Height must be a numeric value.")  # verifica que el número sea numérico
        if value <= 0:
            raise ValueError("Height must be positive.")  # verifica que el número sea positivo
        self._height = value

    @timing_decorator
    def compute_area(self):
        return self._width * self._height
