import math

def carpet(A, B, arena_radius=6.5):

    diagonal = math.sqrt(A**2 + B**2)
    
    d = 2 * arena_radius
    
    return diagonal <= d

A, B = map(float, input().split("x"))

if carpet(A, B):
    print("да")
else:
    print("нет")