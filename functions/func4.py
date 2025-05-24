import math

def circumference(r):
         circum=math.pi*r*r
         area=2*math.pi*r
         return [area,circum]

a,b=circumference(8)
print(f"Area:{math.ceil(a)} Circumference:{math.ceil(b)}")

