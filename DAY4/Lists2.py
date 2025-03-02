# How to access the elements of a list

myList = ["Python","Java","C++"]
print(myList[0]) # Python

# Check if item exists in list or not

if "Ruby" in myList:
    print("Ruby is present in the list")
else:
    print("Ruby is not present in the list")

# Since list are mutable, you can change the value of an item
myList[2] = "C#"
print(myList)

newList = list(("Python","Java","C++","Ruby","HTML","CSS","JavaScript","php"))
newList[3:5]=["C#","SQL"] 
# 3:5 means the 4th and 5th element
print(newList)

myList[1:2]=["Perl","R"]
print(myList)

# if no of items inserted does not match the number of items replaced, the list will extend or shrink
thislist= ["Java","Python","C++"]
thislist[1:3]=["Ruby"]
print(thislist)
# o/p =  ['Java', 'Ruby']

# Now to insert an item
thislist.insert(2,"C#")
print(thislist)

# To append an item
thislist.append("JavaScript")
print(thislist)

# You can extend a llst to another list
myList.extend(thislist)
print(myList)

# pop removes the last element
myList.pop()

myList.remove("Java")
print(myList)
