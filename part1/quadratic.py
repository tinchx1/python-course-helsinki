# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.



a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

x1 = (-b+ sqrt(b ** 2 - 4 * a * c)) / (2*a)
x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2*a)

print(f"The roots are {x1} and {x2}")