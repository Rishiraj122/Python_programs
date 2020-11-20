n=int(input());
li=list(map(int,input().split()));
i=0;
k=1;
Jumpingjack=0;


while(i<n-1):
    if(li[int(i)]<=li[int(k)]):
        i=k;
        Jumpingjack=Jumpingjack+1;

    k=k+1;

print(Jumpingjack);


