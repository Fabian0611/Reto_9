from geometria.point import Point

class Line:
    def __init__(self, start, end):
        if not all(isinstance(point, Point) for point in (start, end)):
            raise TypeError("Start and end must be instances of Point.")  # verifica que los argumentos sean un objeto Point
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def length(self):
        return self._start.compute_distance(self._end)

