# nested condition , in this in if there is another if.

a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print('c is greater')

else:
    print("b is greater")
