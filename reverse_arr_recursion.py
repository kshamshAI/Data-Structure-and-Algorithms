
def reverse(nums, left, right):
    if left>=right:
        return nums
    nums[left],nums[right] = nums[right],nums[left]
    return reverse(nums,left+1,right-1)

arr = [5, 9, 8, 3, 6, 7, 1, 4, 2]
x = reverse(arr,0,8)
print(x)