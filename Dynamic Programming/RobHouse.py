from typing import List
class Solution:
    # recursive approach
    def solve1(self,nums,index):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        pick = nums[index] + self.solve1(nums,index-2) 
        unpick = 0 + self.solve1(nums,index-1) 
        return max(pick,unpick)

    def rob1(self, nums: List[int]) -> int:
        return self.solve1(nums,len(nums)-1)
    
    # memoization
    def solve2(self,nums,index,dp):
        if index == 0:
            return nums[index]
        if dp[index] != -1:
            return dp[index]
        if index < 0:
            return 0
       
        pick = nums[index] + self.solve2(nums,index-2,dp) 

        unpick = 0 + self.solve2(nums,index-1,dp) 
        dp[index] = max(pick,unpick)
        return dp[index]

    def rob2(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)

        return self.solve2(nums,len(nums)-1,dp)
    
    # tabulation
    def rob3(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            pick = nums[i] + dp[i-2] if i > 1 else nums[i]
            unpick = 0 + dp[i-1] 
            dp[i] = max(pick,unpick)
        return dp[len(nums)-1]

    # tabulation with space opt
    def rob4(self,nums:List[int]) -> int:
        prev = nums[0]
        prev2 = 0
        for i in range(1,len(nums)):
            pick = nums[i] + prev2 if i > 1 else nums[i]
            unpick = 0 + prev
            curr = max(pick,unpick)
            prev2 = prev
            prev = curr
        return prev
    



nums1 = [1,2]    
nums = [2,7,9,3,1]
print(Solution().rob2(nums))
print(Solution().rob1(nums))
print(Solution().rob3(nums))
print(Solution().rob4(nums))
