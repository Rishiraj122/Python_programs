print("Enter the Three Sides of the Triangle");
a=int(input(" "));
b=int(input(" "));
c=int(input(" "));


if(a<0 or b<0 or c<0):
    print("Kidding me baby? It can't be negative! Just be Positive Girl!!!")

elif (a==b==c):
    print("This is an Equilateral Triangle")
elif (a==b or a==c or b==c):
    print("This is an Isosceles Triangle")
else:
    print("This is a Scalene Triangle")