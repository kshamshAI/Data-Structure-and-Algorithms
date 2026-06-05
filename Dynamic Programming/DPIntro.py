'''                     ----------------------Introduction to Dynamic Programming--------------------------
Dynamic Programming involves the following steps:
1.Recursion -calling a function itself within a function.Time Complexity-O(2**n) and Space Complexity=O(n) which is stack space
2.Memoization-we can apply memoization where to solve a problem in recursion involves repeated sub-problems so rather than applying recursion every time
for same subproblem instead we store the answer to the subproblem and directly return the value every other  time its used.we store it in an array.
if it requires only one parameter to solve the problem we use 1D-array to store and likewise.By applying memoization we can optimize the time complexity to
O(n) but the space comeplexity is increased by O(n)
3.Tabulation-time complexity remains same but space is optimized by removing stack space used in recursion and rather using some loops.
4.Tabulation with space optimization-time complexity remains same space is optimized to constant space i.e. O(1).
To undersatnd each steps of dynamic programming we take an example of Fibonacci series-0,1,1,2,3,5,8,13,21.........'''

class DynamicProgramming:
   
    def recursion(self,nums):
        # base condition
        if nums <= 1:
            return nums
        return self.recursion(nums-1) + self.recursion(nums-2)
    
    def memoization(self,nums,dp):
          if nums <= 1:
            return nums
          if dp[nums] != -1:
              return dp[nums]
          dp[nums] = self.memoization(nums-1,dp) + self.memoization(nums-2,dp)
          return dp[nums]
    
    def tabulation(self,nums,dp):
        dp[0] = 0
        dp[1] = 1
        for i in range(2,nums+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[nums]
    
    def tabulation_optimized(self,nums):
        prev2 = 0
        prev = 1
        for _ in range(2,nums+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev
nums = 7
dp = [-1]*(nums+1)
obj = DynamicProgramming()
print(obj.recursion(nums))
print(obj.memoization(nums,dp))
print(obj.tabulation(nums,dp))
print(obj.tabulation_optimized(nums))

