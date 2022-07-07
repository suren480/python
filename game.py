
from xml.etree.ElementPath import xpath_tokenizer_re


x=int(input("Enter the value:"))
if x<0:
    print("{0} is negative".format(x))
elif x==0: 
    print("x is zero")
else: 
    print("x is positive")

