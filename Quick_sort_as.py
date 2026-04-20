from Partition_arr import partition
def quick_sort(nums, low, high):
    if (low<high):
        p_index=partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

nums= [4, 1, 7, 6, 3,  2, 8]
n = len(nums)
quick_sort(nums,0,n-1)
print(nums)










