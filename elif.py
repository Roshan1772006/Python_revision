# elif statement in this if there are many condition to check the elif is use

n = int(input("enter your age: "))
if(n>=18):  print(" can vote")
elif(n>=54): print('you are to old to vote')
else: print('invalid for voting')

print("1.RED")
print("2.YELLOW")
print("3.GREEN")
a = int(input("enter the color number: "))
if(a == 1):
    print("stop")

elif(a==2):
    print("Be ready to go")

else:
    print("GO!")
