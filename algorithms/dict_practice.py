# Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two
# arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].
# Your function should have a complexity of O(N). (If your programming
# language has a built-in way of doing this, don’t use it. The idea is to build
# the algorithm yourself.)

def intersection(arr1, arr2):
    bucket = {} 
    intersection_arr = [] 
    for i in range(len(arr1)):
        bucket[arr1[i]] = True 
    
    for i in range(len(arr2)):
        if arr2[i] in bucket:
            intersection_arr.append(arr2[i])
    
    return intersection_arr

# Write a function that accepts an array of strings and returns the first
# duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e",
# "f"], the function should return "c", since it’s duplicated within the array.
# (You can assume that there’s one pair of duplicates within the array.)
# Make sure the function has an efficiency of O(N).

def first_duplicate(arr1):
    seen = {}
    for i in range(len(arr1)):
        if arr1[i] in seen:
            return arr1[i]
        seen[arr1[i]] = True 
    return False 

# Write a function that accepts a string that contains all the letters of the
# alphabet except one and returns the missing letter. For example, the string,
# "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
# except the letter, "f". The function should have a time complexity of O(N).

def find_missing(s):
    alphabet = {chr(i): True for i in range(ord('a'), ord('z') + 1)}
    for c in s:
        if c not in alphabet:
            return c 


# 4. Write a function that returns the first non-duplicated character in a string.
# For example, the string, "minimum" has two characters that only exist
# once—the "n" and the "u", so your function should return the "n", since it
# occurs first. The function should have an efficiency of O(N).
    
def first_occuring(s):
    seen = {}
    for i in range(len(s)):
        if s[i] in seen:
            seen[s[i]] = -1 
        else:
            seen[s[i]] = i 
    
    non_dup_index = {}
    min_index = float('inf')
    print(seen)
    for key, value in seen.items():
        if value != -1:
            min_index = min(value, min_index)
            non_dup_index[value] = key
    
    return non_dup_index[min_index]

print(first_occuring('minimum'))

