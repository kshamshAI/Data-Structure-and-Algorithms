'''Leetcode-45. Jump Game II
Medium
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [2,3,0,1,4]
Output: 2'''
from typing import List
class Solution:
    
        #using recursion
    def func(self,index,jump,n,arr):
        if index >= n-1:
            return jump
        
        mini_jump = float('inf')   
        for i in range(1,+arr[index]+1):
            mini_jump = min(mini_jump,self.func(index+i,jump+1,n,arr))
        return mini_jump
    
    def min_jump(self,arr):
        n = len(arr)
        return self.func(0,0,n,arr)  
    
    # using Greedy algo 

    def jump(self, nums: List[int]) -> int:
        n  = len(nums)
        left = 0
        jump = 0
        right = 0
        farthest = 0
        while right < n-1:
            for i in  range(left,right+1):
                farthest = max(farthest,i+nums[i])
            left = right+1
            right = farthest
            jump+=1
        return jump


        

        
nums = [2,3,1,1,4]
print(f'Minimum jump to reach end:{Solution().jump(nums)}')