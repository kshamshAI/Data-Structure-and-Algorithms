def Insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while(j>=0 and nums[j]>key):
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    return nums

arr = [3, 5, 6, 4, 8, 9, 10, 7, 1]
x = Insertion_sort(arr)
print(x)