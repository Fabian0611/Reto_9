from geometria.point import Point
from geometria.rectangle import Rectangle
from geometria.square import Square
from geometria.triangle import Triangle
from geometria.equilateral import Equilateral
from geometria.isosceles import Isosceles
from geometria.scalene import Scalene
from geometria.tri_rectangle import TriRectangle
from geometria.shape import Shape

if __name__ == "__main__":
    try:
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(1, 2)

        figura = Shape([])
        print(f"Shape:\n{'-'*40}\nOriginal Shape Type: {figura.shape_type}")
        Shape.set_shape_type("Polygon")
        print(f"New Shape Type: {figura.shape_type}\n")

        rectangle = Rectangle(p1, 4, 3)
        print(f"Rectangle:\n {'-'*40}")
        rect_area = rectangle.compute_area()
        print(f"Rectangle Area: {rect_area}")
        print(f"Rectangle Perimeter: {rectangle.compute_perimeter()}\n")

        square = Square(p1, 4)
        print(f"Square:\n {'-'*40}")
        square_area = square.compute_area()
        print(f"Square Area: {square_area}")
        print(f"Square Perimeter: {square.compute_perimeter()}\n")

        triangle = Triangle([p1, p2, p3])
        print(f"Triangle:\n {'-'*40}")
        triangle_area = triangle.compute_area()
        print(f"Triangle Area: {triangle_area}")

        tri_equilateral = Equilateral([p1, p2, p3])
        print(f"Is Equilateral?: {tri_equilateral.is_equilateral()}")

        tri_isosceles = Isosceles([p1, p2, p3])
        print(f"Is Isosceles?: {tri_isosceles.is_isosceles()}")

        tri_scalene = Scalene([p1, p2, p3])
        print(f"Is Scalene?: {tri_scalene.is_scalene()}")

        tri_rectangle = TriRectangle([p1, p2, p3])
        print("Is Right Triangle:", tri_rectangle.is_right_triangle())

    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")