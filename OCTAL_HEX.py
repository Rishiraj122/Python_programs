x=input("Enter a number");
x=int(x);
print("HEX to convert the number to HEXADECIMAL");
print("OCT to convert the number to OCTAL");
choice=input("Enter Your Choice ");
if(choice=='HEX'):
    print(hex(x).lstrip("0x"));
elif(choice=='OCT'):
    print(oct(x).lstrip("0xo"));
else:
    print("ERROR");

#The lstrip() removes characters from the left based on the argument.
#The hex() method is used to convert binary to hexadecimal
#The oct() method is used to convert binary to octal.