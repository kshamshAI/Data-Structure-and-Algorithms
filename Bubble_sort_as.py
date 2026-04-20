def Bubble_sort(nums):
    for i in range(len(nums)-2,-1,-1):
        is_swap = False
        for j in range(0, i+1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap = True
        if(is_swap == False):
            break
    return nums

arr = [5, 8, 1, 6, 9, 2, 4]
x = Bubble_sort(arr)
print(x)