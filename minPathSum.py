from typing import List
import sys
class Solution:
   
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def solve(i,j,grid):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')
            up_sum =  solve(i-1,j,grid)
            left_sum = solve(i,j-1,grid)
            return grid[i][j] + min(up_sum,left_sum)
        return solve(m-1,n-1,grid)
       
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        def solve(i,j,grid,dp):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            up_sum =  solve(i-1,j,grid,dp)
            left_sum = solve(i,j-1,grid,dp)
            dp[i][j] = grid[i][j] + min(up_sum,left_sum)
            return dp[i][j]
        return solve(m-1,n-1,grid,dp)
    
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i < 0 or j < 0:
                    dp[i][j]= float('inf')
                    continue
                up_sum = dp[i-1][j]
                left_sum = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up_sum,left_sum)
            return dp[m-1][n-1]
    def minPathSum3(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up_sum = dp[i-1][j] if i > 0 else float('inf')
                left_sum = dp[i][j-1] if j>0 else float('inf')
                dp[i][j] = grid[i][j] + min(up_sum,left_sum)
        return dp[m-1][n-1]
    
    def minPathSum4(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = [0]*n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[0] = grid[0][0]
                    continue
                else:
                    up_sum = prev[j] if i > 0 else float('inf')
                    left_sum = curr[j-1] if j>0 else float('inf')
                curr[j] = grid[i][j] + min(up_sum,left_sum)
            prev = curr.copy()
        return prev[n-1]


      
    
       
        
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum1(grid))
print(Solution().minPathSum2(grid))
print(Solution().minPathSum3(grid))

 