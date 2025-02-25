# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# SOURCE: https://leetcode.com/problems/longest-common-prefix/

def twoSum(self, nums, target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
                
nums=[3,2,4]
print(twoSum(nums,6))
nums=[2,7,11,15]
print(twoSum(nums,9))
nums[3,3]
print(twoSum(nums,6))


       
        