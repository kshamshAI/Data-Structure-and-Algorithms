# Leetcode Problem-1004
'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length'''
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        right = 0
        zeros = 0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left +=1
               
            if zeros <= k:
                maxi = max(maxi,right-left+1)
            right += 1
        return maxi

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(f'max_consecutive ones flipping max {k} zeros to one:{Solution().longestOnes(nums,k)}')# Leetcode Problem-1004
'''Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length'''
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        right = 0
        zeros = 0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left +=1
               
            if zeros <= k:
                maxi = max(maxi,right-left+1)
            right += 1
        return maxi

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(f'max_consecutive ones flipping max {k} zeros to one:{Solution().longestOnes(nums,k)}')