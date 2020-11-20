
testcases=int(input());

for j in range(0,testcases):
    lst=[]
    sum=0;
    n=int(input());

    lst = [int(x) for x in input().split()]

    lst.sort();

    temp=lst[n-1];
    lst[n-1]=lst[0];
    lst[0]=temp;

    for i in range(0,n-1):
        x=lst[i]-lst[i+1];

        if x<0:
            x=x*(-1);
        sum=sum+x;

    x=lst[0]-lst[n-1];

    if x<0:
        x=x*(-1);
    sum=sum+x;

    print(sum)