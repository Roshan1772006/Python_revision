# for loop , in this a code which is repeatly run till the condition is not false

n =int(input("Enter a number: "))
for i in range(n): # range function is use it make declaration for 0-n
    print(i)

s = str(input("Enter a number: "))  
for i in  range(len(s)): # len() function is use to find the number of character a string contain
    print(s[i])