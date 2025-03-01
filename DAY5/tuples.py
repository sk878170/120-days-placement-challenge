# Tuples are similar to list, but they are immutable
# Represented by curly brackets
# allows duplicate values
# Ordered

myTuple=("Python","Java","C++","C#")
print(myTuple)
print(myTuple[2]) # 3rd element

# NOTE: You cannopt create a tuple with 1 item

singleTuple = ("Python")
print(type(singleTuple)) # <class 'str'>

singleTuple = ("Python",) # Inserting a , at end to make it a tuple
print(type(singleTuple)) # <class 'str'>

# A tuple can contain different data types
mixedTuple = ("Python",1,2.5)
print(mixedTuple)

# Creating a tuple using tuple constructor
newTuple = tuple(("Python", "java", "C++"))

