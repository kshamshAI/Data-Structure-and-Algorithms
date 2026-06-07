'''Leetcode--------------63. Unique Paths II
Solved
Medium
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1'''


from typing import List
class Solution:
    #recursion
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:    
        def solve(i,j,obstacleGrid):
            if i == 0 and j == 0:
                if obstacleGrid[i][j] == 1:
                    return 0
                return 1
            if i < 0 or j <0:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            up = solve(i-1,j,obstacleGrid)
            left = solve(i,j-1,obstacleGrid)
            return up + left
        return solve(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid)
    #memoization
    def uniquePathsWithObstacles12(self, obstacleGrid: List[List[int]]) -> int:   
        dp = [[-1]*(len(obstacleGrid[0])) for _ in range(len(obstacleGrid))] 
        def solve(i,j,obstacleGrid,dp):
            if i == 0 and j == 0:
                if obstacleGrid[i][j] == 1:
                    return 0
                return 1
            if i < 0 or j <0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if obstacleGrid[i][j] == 1:
                return 0
            up = solve(i-1,j,obstacleGrid,dp)
            left = solve(i,j-1,obstacleGrid,dp)
            dp[i][j]  = up + left
            return dp[i][j]
        return solve(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid,dp)
    

    # Tabulation
    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int:   
        dp = [[-1]*(len(obstacleGrid[0])) for _ in range(len(obstacleGrid))] 
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                dp[i][j] = up + left
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
  
    def uniquePathsWithObstacles4(self, obstacleGrid: List[List[int]]) -> int:   
        prev = [0]*len(obstacleGrid)
        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(len(obstacleGrid)):
            curr = [0]*len(obstacleGrid[0])
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    curr[j] =0
                    continue
                elif i == 0 and j == 0:
                    curr[0] = 1
                else :
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr.copy()
        return prev[len(obstacleGrid[0])-1]


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().uniquePathsWithObstacles1(obstacleGrid))
print(Solution().uniquePathsWithObstacles12(obstacleGrid))
print(Solution().uniquePathsWithObstacles3(obstacleGrid))
print(Solution().uniquePathsWithObstacles4(obstacleGrid))