import math


def exercsie_1(r):
    diameter = 2 * r
    print("Diameter of a circle (2r) = ", diameter)
    area = math.pi * r ** 2
    print("The area of a circle (πr2) = ", area)
    circum = 2 * math.pi * r
    print("The circumference of a circle (2πr)", circum)
    sphere = 4 * math.pi * r ** 2
    print("The area of a sphere (4πr2)", sphere)

    volofsphere = 4 / 3 * math.pi * r**3
    print(volofsphere)


if __name__ == "__main__":
    exercsie_1(r=3.2)
