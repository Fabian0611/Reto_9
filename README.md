# Reto_9

1. Add the @property decorator into the package Shape, so all the protected data could be accessed this way.
2. Add @classmethod decorator to Shape, in order to change define and change the type of shape of each class.
3. Add a custom decorator in Shape co show the computation time of at least one operation. e.g: compute_area.

## Codigo

- En el codigo se utilizaron los decoradores de property y de setter en intercambio de los getters y setters convencionales.
- Se creo un "atributo" en la clase shape para poder hacer uso del decorador classmethod y poder cambiar este atributo de la clase.
- Por ultimo se anadio el decorador timing para calcular el tiempo que se demora cada clase en calcular compute_area().

A continuacion se pone la clase shape que evidencia los tres decoradores usados.
```python
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
```
## Output
Este es el resultado final que bota en la terminal

```bash
Shape:
----------------------------------------
Original Shape Type: Any Shape
New Shape Type: Polygon

Rectangle:
 ----------------------------------------        
Execution time for compute_area: 0.000002 seconds
Rectangle Area: 12
Rectangle Perimeter: 14.0

Square:
 ----------------------------------------        
Execution time for compute_area: 0.000003 seconds
Square Area: 16
Square Perimeter: 16.0

Triangle:
 ----------------------------------------
Execution time for compute_area: 0.000008 seconds
Triangle Area: 2.0
Is Equilateral?: False
Is Isosceles?: True
Is Scalene?: False
Is Right Triangle: False
```
