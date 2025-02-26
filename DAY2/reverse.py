# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


def reverseInt(x):
    if -2**31<x<2**31:
        rev=0
        while x!=0:
            rev=(rev*10)+(x%10)
            x=x//10
        return rev
    else:
        return 0

x=2**45
print(reverseInt(x)) 
x=123
print(reverseInt(x))  # Output: 321
