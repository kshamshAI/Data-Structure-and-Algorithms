from Merge_arr import merge_arr

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