# Leetcode Problem--35 -Search Insert Position in array
'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104'''

def search_pos(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    lb = n
    while low <=high:
        mid = (low + high)//2
        if arr[mid] >= target:
            lb = mid
            high = mid-1 
        else:
            low = mid + 1
    return lb

print(search_pos( [1,3,5,6], target = 7))