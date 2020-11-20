import math
pie=math.pi
def Volume(x):
    return (4/3)*pie*pow(x,3);
r=int(input("Enter the radius of the Sphere: "))
v=Volume(r)
print(v);