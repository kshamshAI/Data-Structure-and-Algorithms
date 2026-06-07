'''Leetcode-------------------------------213. House Robber II
Solved
Medium
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:
Input: nums = [1,2,3]
Output: 3
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000'''
from typing import List
class Solution:
    # recursion
    def solve(self,nums,index):
        if index == 0:
            return  nums[0]
        if index < 1:
            return 0
        pick = nums[index] + self.solve(nums,index-2)
        unpick = 0 + self.solve(nums,index-1)
        return max(pick,unpick)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        ans1 = self.solve(nums[:n-1],n-2)
        ans2 = self.solve(nums[1:],n-2)
        return max(ans1,ans2)
    
    # memoization 
    def solve1(self,nums,index,dp):
        if index == 0:
            return  nums[0]
        if index < 1:
            return 0
        if dp[index] != -1:
            return dp[index]
        pick = nums[index] + self.solve1(nums,index-2,dp)
        unpick = 0 + self.solve1(nums,index-1,dp)
        dp[index] = max(pick,unpick)
        return dp[index]

    def rob1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1] * (n-1)
        n = len(nums)
        ans1 = self.solve1(nums[:n-1],n-2,dp)
        dp = [-1] * (n-1)
        ans2 = self.solve1(nums[1:],n-2,dp)
        return max(ans1,ans2)
    
    # tabulation
    def tabulation(self,nums):
        n = len(nums)
        
        dp = [-1] * (n)
        dp[0] = nums[0]
        for i in range(1,n):
            pick = nums[i] + dp[i-2] if i>1 else nums[i]
            unpick = 0 + dp[i-1]
            dp[i] = max(pick,unpick)
        return dp[n-1]
    
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        ans1 = self.tabulation(nums[:n-1])
        dp = [-1] * (n-1)
        ans2 = self.tabulation(nums[1:])
        return max(ans1,ans2)
    

    # tab with opt
    def tabulation(self,nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1,n):
            pick = nums[i] + prev2 if i>1 else nums[i]
            unpick = 0 + prev
            curr = max(pick,unpick)
            prev2 = prev 
            prev = curr
        return prev
    
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        ans1 = self.tabulation(nums[:n-1])
        ans2 = self.tabulation(nums[1:])
        return max(ans1,ans2)


