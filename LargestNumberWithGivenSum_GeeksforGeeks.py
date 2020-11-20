def sumofDigits(n):
    temp=0;
    while(n!=0):
        temp=temp+int(n%10);
        n=int(n/10);
    return temp;

for i in range(int(input())):
    n,k=input().split();
    n=int(n);
    k=int(k);
    x=10**(n);
    y=10**(n-1);
    flag=0;

    for j in reversed(range(y,x)):
        if(sumofDigits(j)==k and flag==0):
            print(j);
            flag=1;
        
    if(flag==0):
        print(-1);