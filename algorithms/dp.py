def fib(n, memo={}):
    if n == 0 or n == 1:
        return n 
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))

def add_until_100(arr):
    if len(arr) == 0: return 0 
    total_without_curr = add_until_100(arr[1:])
    if arr[0] + total_without_curr > 100:
        return total_without_curr
    else:
        return total_without_curr + arr[0]
print(add_until_100([1,2,3,4,101]))

def golomb(n, memo={1: 1}):
    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n-1)))
    return memo[n]

def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1 
    if (rows, columns) not in memo:
        memo[(rows,columns)] = unique_paths(rows-1,columns, memo) + unique_paths(rows,columns-1, memo)
    return memo[(rows, columns)]