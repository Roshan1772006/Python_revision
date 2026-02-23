#  Lists are used to store multiple items in a single variable.

list = [1,'two',3,'four',5,'six',7,'eight',9,'ten']
list1 = [11,12,13,14]
print(list)   # display all element of list

# for access the a particular value for a list it is done by indexing
print(list[5])

# for access the a range of value from list we use silceing 
print(list[0:5])

#  you can remove a value form the list
list.remove(3)
print(list)

list1.clear()
print(list1)

list.pop()
print(list)

del(list[2])
print(list)

# for insert a value at last
list.append(11)
print(list)

# for insert a value at particular index
list.insert(2,"ro")
print(list)


# as name say extend a list by adding twolist
list.extend(list1)
print(list)

list2 = [5,9,3,4,1,2,0]
list2.sort()
print(list2)