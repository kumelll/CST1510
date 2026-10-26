from math import tan, pi

side = float(input("Enter the side length: "))

area = 5 * side ** 2 / (4 * tan(pi / 5))

print(f"Area = {area:.2f}")
