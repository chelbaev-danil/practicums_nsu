import math
a = int(input())
b = int(input())
c = int(input())

DegA = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
DegB = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
DegC = 180 - DegA - DegB

print(DegA)
print(DegB)
print(DegC)

