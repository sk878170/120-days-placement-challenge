# Palindrome check
# A palindrome is a number, which if reversed then remains the same
# eg. 121 -> 121 or 1234321 -> 1234321

def Palindrome_Check(x):
    if x<0:
        return False
    else:
        copy=x
        rev=0
        while x != 0:
            rev=(rev*10)+(x%10)
            x=x//10
        return copy == rev
        
x=121
print(Palindrome_Check(x))
y=123
print(Palindrome_Check(y))
