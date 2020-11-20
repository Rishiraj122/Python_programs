val=input("Enter the value ")
li=[]
j=0;
x=val.split("[")
for i in x:
    if(i!='[' or i!=']'):
        li.insert(i,j);
        j=j+1


for i in li:
    print(li)