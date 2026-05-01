# Write a program to sort an array using Quick sort.........................
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while (i < j):
        while(pivot <= arr[i]) and (i <= high - 1):
            i += 1
        while(pivot > arr[j]) and (j <= low + 1):
            j -=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

def quick_sort(arr,low,high):
    if low < high:
        p_index = partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

nums = [4,7,3,6,7,1,9,8,5]
l = 0
h = len(nums)-1
quick_sort(nums,l,h)
print(nums)



    