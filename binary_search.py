# Implementation of binary search:---------------------

# Optimal Approach--- Time Complexity=O(NlogN base 2) , Space Complexity=O(1)
def binary_search(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    
    while low < high:
        mid = low + high //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1



# Recursive Approach--- Time Complexity=O(N), for 32 elements log 2**5 base 2= 5 , Space Complexity=O(N)-stack space

def binary_search(arr,low,high):
    mid = low + high // 2
    if low > high:
        return -1
    elif low < high:
         binary_search(arr,mid+1,high)
    else:
         binary_search(arr,low,mid)

    
# Implementation of Lower bound and Upper bound in Binary Search-------Time Complexity-O(log N base 2)--------------------------

# Lower Bound - Smallest index for nums[mid] >= target
def lower_bound(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    lb = n
    while low <=high:
        mid = low + high//2
        if arr[mid] >= target:
            lb = mid
            high = mid-1 
        else:
            low = mid + 1
    return lb

# Upper Bound - Smallest index for nums[mid] > target
def upper_bound(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    ub = n
    while low <=high:
        mid = low + high//2
        if arr[mid] > target:
            ub =  mid
            high = mid-1
        else:
            low = mid + 1
    return ub