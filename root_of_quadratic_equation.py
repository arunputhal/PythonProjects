import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

r1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
r2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

print(f"The roots value are: {r1} and {r2}")

