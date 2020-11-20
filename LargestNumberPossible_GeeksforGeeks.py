for i in range(int(input())):
    n,k=input().split();
    n=int(n);
    k=int(k);
    sum=0;
    arr=[];
    if(k>9*n):
        print(-1);
    else:
        for j in range(0,n):
            if(k>9):
                arr.append(9);
                k=k-9;
            elif(k>-1 and k<=9):
                arr.append(k);
                k=0;
            
            sum=sum+arr[j]*(10**(n-j-1));
        print(sum);
        