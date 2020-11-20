for i in range(int(input())):
    n,k=input().split();
    n=int(n);
    k=int(k);
    arr=[];

    arr = list(map(int, input().split()))

    for j in range(k,n):
        print(arr[j], end=' ');

    for j in range(0,k):
        print(arr[j], end=' ');
    
    print();