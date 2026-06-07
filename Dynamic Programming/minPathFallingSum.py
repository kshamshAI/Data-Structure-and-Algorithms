'''Leetcode----------931. Minimum Falling Path PathSum
Solved
Medium
Given an n x n array of integers matrix, return the minimum Pathsum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum Pathsum as shown.
Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum Pathsum is shown.
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100'''
from typing import List
class Solution:
    # recursion
    def minFallingPathSum1(self,grid:List[List[int]]) ->int:
        n = len(grid)
        def solve(i,j,grid,n):
            if j < 0 or j >= n:
                return float('inf')
            if i == 0:
                return grid[0][j]
            down = grid[i][j] + solve(i-1,j,grid,n)
            left_dia = grid[i][j] + solve(i-1,j+1,grid,n)
            rt_dia = grid[i][j] + solve(i-1,j-1,grid,n)
            return min(down,rt_dia,left_dia)
        
        mini = float('inf')
        for k in range(0,n):
            mini= min(mini,solve(n-1,k,grid,n))
        return mini
  
    # memoization
    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[None]*n for _ in range(n)]
        def solve(i,j,matrix,n,dp):
            if j < 0 or j >= n:
                return float('inf')
            if i == 0:
                return matrix[0][j]
            if dp[i][j] != None:
                return dp[i][j]
            up = matrix[i][j] + solve(i-1,j,matrix,n,dp)
            left_dia = matrix[i][j] + solve(i-1,j-1,matrix,n,dp)
            right_dia = matrix[i][j] + solve(i-1,j+1,matrix,n,dp)
            dp[i][j] = min(up,left_dia,right_dia)
            return dp[i][j]
        mini = float('inf')
        for j in range(n):
            mini = min(mini,solve(n-1,j,matrix,n,dp))
        return mini
    
    # tabulation
    def minFallingPathSum3(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        for k in range(n):
            dp[0][k] = matrix[0][k] 
        for i in range(1,n):
            for j in range(n):
                up =   matrix[i][j] + dp[i-1][j]
                left_dia =float('inf') if j == 0  else matrix[i][j] + dp[i-1][j-1]
                right_dia =   float('inf') if j == n-1  else matrix[i][j] + dp[i-1][j+1]  
                dp[i][j] = min(up,left_dia,right_dia)
        return min(dp[n-1])
    
    # tabulation with space optimized
    def minFallingPathSum4(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = [0]*n
        for k in range(n):
            prev[k] = matrix[0][k] 
        for i in range(1,n):
            curr = [0]*n
            for j in range(n):
                up =   matrix[i][j] + prev[j]
                left_dia =float('inf') if j == 0  else matrix[i][j] + prev[j-1]
                right_dia =   float('inf') if j == n-1  else matrix[i][j] + prev[j+1]  
                curr[j] = min(up,left_dia,right_dia)
            prev = curr.copy()
        return min(prev)
 
        
    
    
grid = [[2,1,3,9],
        [6,5,4,14],
        [7,8,9,19],
        [1,14,20,24]]

print(Solution().minFallingPathSum1(grid))
print(Solution().minFallingPathSum2(grid))
print(Solution().minFallingPathSum3(grid))
print(Solution().minFallingPathSum4(grid))