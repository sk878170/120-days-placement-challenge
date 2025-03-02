# Write a function to find the longest common prefix string amongst an array of strings.


def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string in the list as the prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            # Reduce the prefix by one character at a time
            prefix = prefix[:-1]
        if not prefix:
            break
    
    return prefix

strs=["flower","flow","flight"]
print(longest_common_prefix(strs)) # Output: "fl"
strs=["dog","racecar","car"]
print(longest_common_prefix(strs)) # Output: ""
strs=["ab","a"]
print(longest_common_prefix(strs)) # Output: "a"
    