# Python has following data types
# str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, nonetype
#  We are gonna implement all these data types

x="hello World" #str (immutable)
print(type(x))
print(x)

x=20 # int (immutable)
print(type(x))
print(x)

x=20.0 # float (immutable)
print(type(x))
print(x)

x=1j # complex (immutable)
print(type(x))
print(x)

x=range(6) # range (immutable)
print(type(x))
print(x)

x = ['Football',"Cricket","tennis"] # list (mutable)
print(type(x))
print(x)

x = {"name":"xyz","Age":36} # dict (mutable)
print(type(x))
print(x)

x = {"Red","blue","green"} # set (mutable & unique)
print(type(x))
print(x)

x = frozenset({"Red","blue","green"}) # frozenset (immutable)
print(type(x))
print(x)

x = True # boolean (immutable) 
print(type(x))
print(x)

x=b"hello" # bytes (immutable)
print(type(x))
print(x)

x = bytearray(5) # (mutable)
print(type(x))
print(x)

x=memoryview((bytes(5))) # (mutable)
print(type(x))
print(x)

x = None
print(type(x)) #(immutable)
print(x)


