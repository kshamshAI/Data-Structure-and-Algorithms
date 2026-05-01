# Write a program to calculate max sub-array sum?.....
# sub-array is a subset of original array with consecutive elements in it.

# Brute force Approach--TC = O(N**2)
def max_subarray(arr):
    
    maxim = float('-inf')
    for i in range(0,len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum = sum + arr[j]
            if sum > maxim:
                maxim = sum
    return maxim


# Optimal Approach--TC = O(N)
def max_subarray_opt(arr):
    sum = 0
    maxi = float('-inf')
    for i in range(0,len(arr)):
        sum = sum + arr[i]
        maxi = max(sum,maxi)
        if sum < 0:
            sum = 0
    return maxi
        

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_opt(nums))
