filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
newfilenames=[]
i=0
# using as many lines of code as your chosen method requires.
for x in filenames:
    if x.endswith(".hpp"):
        newfilenames.append(x[:-2]);
    else:
        newfilenames.append(x);

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]