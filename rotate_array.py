# Write a program to rotate an array by 'k'?
# e.g. if arr = [2,4,2,5,7,4,8,9] and k = 3
# ans = [4,8,9,2,4,2,5,7]

def reverse_arr(arr,left,right):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1

nums = [1,6,3,6,9,4,3,2,7,1,5]
n = len(nums)
k = 3
reverse_arr(nums,0,n-k-1)
reverse_arr(nums,n-k,n-1)
reverse_arr(nums,0,n-1)
print(nums)