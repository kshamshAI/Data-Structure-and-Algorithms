# First and Last Occurence  of target in an array--------- -> list[<index1>,<index2>]
class Solution:
    def __init__(self,arr,target):
        self.arr = arr
        self.target = target

    def first_occurence(self,arr,target):
        n = len(arr)
        low = 0
        high = n-1
        first = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] >= target:
                first = mid
                high = mid - 1
            else:
                low = mid + 1

                
        return first


    def last_occurence(self,arr,target):
        n = len(arr)
        low = 0
        high = n-1
        last = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return last
    
    def first_last(self,arr,target):
        first = self.first_occurence()
        last = self.last_occurence()
        return [first,last]

nums = [1,1,1,2,2,3,3,3,5,5,5,5,5,7,8,9]
print(first_last(nums,6))