
for i in range(int(input())):

    n,k=input().split();
    n=int(n);
    k=int(k);

    li=list(map(int,input().split()));

    li.sort();
    count=0;

    for i in li:    
        if(k>=int(i)):
            k=k-int(i);
            count=count+1;
    print(count);