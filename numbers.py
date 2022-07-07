x=int(input("Enter the value:"))
y=int(input("Enter the value:"))
z=int(input("Enter the value:"))
if x>y and x>z:
    print("x {0}The highest value is:".format(x))
elif y>x and y>z: 
    print("y {0}The highest value is is:".format(y))
    
else:
    print("z {0}The highest value is is:".format(z))