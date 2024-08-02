def binary_search(arr, value):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (r + l) // 2 
        if arr[m] < value:
            l = m + 1 
        elif arr[m] > value:
            r = m - 1
        else:
            return True 
    return False 


arr = [1,2,3,4,5]
print(binary_search(arr, 2)) ##True 
print(binary_search(arr, 6)) ##False 
