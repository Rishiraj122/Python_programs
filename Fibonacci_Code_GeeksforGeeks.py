def fibonacci(n):
    if(n<=1):
        return n;
    else:
        return fibonacci(n-1)+fibonacci(n-2);

for i in range(int(input())):
    k=int(input());
    for j in range(1,k+1):
        print(fibonacci(j), end=' ');
    print();