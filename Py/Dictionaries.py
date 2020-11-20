wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for keys,values in wardrobe.items():
    	for i in values:
		    print("{} {}".format(i,keys))