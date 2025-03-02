# Changing a value in tuple is not possoble as it is immutable.
# but you can converyt it into a list then change its values and then convert it back to tuple

x = ("Python", "Java", "C++", "C#")
print(type(x))

# convert into a list
x = list(x)
print(type(x))

# update
x[2] = "JavaScript"

# insert
x.append("Ruby")

# remove an item
x.remove("C#")

# back to a tuple
x = tuple(x)
print(type(x))
print(x)


# You can although add a tuple to another tuple
newTuple = ("HTML", "CSS", "JavaScript")
x += newTuple
print(x)
