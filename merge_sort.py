# Write a program to sort an array using merge_sort?.................

def merge_arr(left_arr,right_arr):
    m = len(left_arr)
    n = len(right_arr)
    i = 0
    j = 0
    result = []
    while (i < m) and (j < n):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i +=1
        else:
            result.append(right_arr[j])
            j +=1
    if i < n :
        while(i < n):
             result.append(left_arr[i])
             i +=1
    if j < m :
        while(j < m) :
            result.append(right_arr[j]) 
            j +=1
    return result

def merge_sort(arr):
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    if len(arr) == 0 or len(arr) == 1:
        return arr
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    result = merge_arr(left,right)
    return result
    
    
nums = [1,2,5,9,8,4,1,3,6]
x = merge_sort(nums)
print(x)

