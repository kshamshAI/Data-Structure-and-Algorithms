def merge_arr(left, right):
    result = []
    i=0 
    j = 0
    m = len(right)
    n = len(left)
    while(i < n and j < m):
        if(left[i]> right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if(i < n):
        while(i<n):
            result.append(left[i])
            i+=1
    if(j < m):
        while(j<m):
            result.append(right[j])
            j+=1
    return result

def merge_sort(nums):
    if(len(nums) <= 1):
        return nums
    n = len(nums)
    mid = n//2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_arr(left, right)

 
x =merge_sort([3, 1, 2, 4, 1, 5, 2, 6, 4])
print(x)
