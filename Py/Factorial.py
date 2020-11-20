import math
for j in range(int(input())):
    flag=0;
    num = input("") 
    def recur_factorial(n):
        if n == 1:
            return n
        elif n < 1:
            return ("NA")
        else:
            return n*recur_factorial(n-1)

    repeat=recur_factorial(int(num))
    repeat=str(repeat);
    for i in repeat[::-1]:
        if(int(i)!=0 and flag!=1):
            print(i)
            flag=1

