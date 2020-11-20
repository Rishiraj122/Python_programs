import timeit

listtime_test=timeit.timeit(stmt="[1,2,3,4]",number=1000000)
tupletime_test=timeit.timeit(stmt="(1,2,3,4)",number=1000000)

print("LIST TIME: ",listtime_test);
print("TUPLE TIME: ",tupletime_test);

#This is used to compare the time.
#The stmt is used to create a short LIST or a short TUPLE
#The number shows the number of times it'll be executed

