# Floor and ceilm of a given target in an array----> list[<floor>,<ceil>]

def floor_ceil(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    floor = -1 
    ceil  = -1
    while low <=high:
        mid = (low + high)//2
        if arr[mid] == target:
            return [arr[mid],arr[mid]]
        elif arr[mid] > target:
            ceil = arr[mid]
            high = mid-1 
        else:
            floor = arr[mid]
            low = mid + 1
    return [floor,ceil]

nums = [3,4,4,5,7,8,9,10,12,15]

print(floor_ceil(nums,2))