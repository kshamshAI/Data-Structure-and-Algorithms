'''62. Unique Paths
Solved
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down'''
class Solution:
    #memoization
    # def solve(self,m,n,row_index,col_index,dp):
    #     if row_index==0 and col_index==0:
    #         return 1
    #     if row_index<0 or col_index < 0 :
    #         return 0
    #     if dp[row_index][col_index] != -1:
    #         return dp[row_index][col_index]
       
    #     up =    self.solve(m,n,row_index-1,col_index,dp)
    #     left = self.solve(m,n,row_index,col_index-1,dp)
    #     dp[row_index][col_index] = up + left
        
    #     return dp[row_index][col_index]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[-1]*n for _ in range(m)]
    #     return self.solve(m,n,m-1,n-1,dp)

    
    #tabulation
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[-1]*n for _ in range(m)]
    #     dp[0][0] = 1
    #     for row in range(0,m):
    #         for col in range(0,n):
    #             if row == 0 and col == 0:
    #                 continue
               
    #             up = dp[row-1][col] if row > 0 else 0
    #             left = dp[row][col-1] if col > 0 else 0
    #             dp[row][col] = up + left
    #     return dp[m-1][n-1]

    # tabulation opt
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0]*m
        for row in range(0,m):
            curr = [0]*n
            for col in range(0,n):
                if row == 0 and col == 0:
                    curr[0] = 1
                else: 
                    up = prev[col] if row > 0 else 0
                    left = curr[col-1] if col > 0 else 0
                    curr[col] = up + left
            prev = curr.copy()
        return prev[n-1]
            
                
       
        