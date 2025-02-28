import time
from .rectangle import Rectangle

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


class Square(Rectangle):
    def __init__(self, bottom_left, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise TypeError("Side length must be a positive numeric value.")  # verifica que el número sea válido
        super().__init__(bottom_left, side_length, side_length)

    @timing_decorator
    def compute_area(self):
        return self._width * self._height
