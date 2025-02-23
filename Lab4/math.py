import math


def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree = float(input("Input degree: "))
print(f"Output radian: {degree_to_radian(degree):.6f}")


def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input("\nHeight: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

print(f"Expected Output: {trapezoid_area(height, base1, base2)}")


def regular_polygon_area(n, side_length):
    return (n * side_length**2) / (4 * math.tan(math.pi / n))

n = int(input("\nInput number of sides: "))
side_length = float(input("Input the length of a side: "))

print(f"The area of the polygon is: {regular_polygon_area(n, side_length):.2f}")


def parallelogram_area(base, height):
    return base * height

base = float(input("\nLength of base: "))
height = float(input("Height of parallelogram: "))

print(f"Expected Output: {parallelogram_area(base, height):.2f}")
