# Write a program to sort an array using insertion sort??..................

# Ascending order
def insertion_sort(nums):
    n = len(nums)
    
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while(nums[j] > key) and (j>=0):
            nums[j+1] = nums[j]
            j -=1
        nums[j+1] = key
        
    return nums

# Descending order
def insertion_dsc(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while(j>=0) and nums[j]<key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


arr = [1,9,7,5,6,9,4,3]
x = insertion_dsc(arr)
print(x)