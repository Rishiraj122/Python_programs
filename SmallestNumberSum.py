import math

def sumofdigits(n):

    if(n==0):
        print("0", end="");
    
    if(n%9!=0):
        print(n%9, end="");

    for i in range(1, int(n/9)+1):
        print("9", end="");
    
    for i in range(1,n+1):
        print("0",end="");
    
    print();

for j in range(int(input())):
    
    n=int(input());
    sumofdigits(n);