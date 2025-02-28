# Remove duplicate vallues from a sorted array and return the number of unique elements

# example: nums=[1,1,2]
# output: 2 
# [1,2]

# example2: nums=[0,0,1,1,2,2,3,3,4]
# output: 5
# [0,1,2,3,4]

def removeDuplicates(nums):
    u=0 # U is the last unique element
    for i in range(1,len(nums)):
        if nums[u]!=nums[i]:
            nums[u+1]=nums[i]
            u+=1
    return u+1

nums=[1,1,2]
res=removeDuplicates(nums)
print(res)

nums=[0,0,1,1,2,2,3,3,4]
res1=removeDuplicates(nums)
print(res1)
    
