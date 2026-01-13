import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    return 0.0

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    return ""

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""

    for i in range(n):

        for j in range(i):
            result += " "

        for k in range(2 * (n - i - 1) - 1):
            result += "*"

        result += "\n"

    return result.rstrip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
