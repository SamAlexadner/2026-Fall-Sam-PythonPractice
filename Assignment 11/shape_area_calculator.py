# from shape import Shape
from shape import CircleShape
from shape import RectageleShape
from shape import SquareShape
from shape import TriangleShape


def main():
    shapes = [        
        RectageleShape("Rectangle", 5, 4),
        CircleShape("Circle", 3),
        SquareShape("Square", 4),
        TriangleShape("Triangle", 3, 2),
        ]


    print("Areas of various shapes:")
    for shape in shapes:  # polymorphism: each shape computes its own area
        print(f"{shape.__class__.__name__} area: {shape.get_area():.2f}")


if __name__ == "__main__":
    main()