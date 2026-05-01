# Write a program to arrange an array in alternate sign sequence?

def arrange(arr):
    result = [0] * len(arr)
    p = 0 
    n = 1
    for i in range(0,len(arr)):
        if arr[i] >= 0:
            result[p] = arr[i]
            p +=2
        else:   
            result[n] = arr[i] 
            n +=2

    return result

nums = [2,9,-4,5,-7,9,-3,-1]
print(arrange(nums))