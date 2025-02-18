# area of regular polygon
import math
n = int(input())
a = int(input())
s =( n * a**2) / (4 * math.tan(math.pi/n))
s = s(round)
print(f"The area of the polygon is:{s}")