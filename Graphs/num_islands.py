'''Leetcode Problem-200--------------------- Number of Islands
Medium
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
Output: 1
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
Output: 3
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.'''

#-------------------------------Solution--------------------------------------------------------

from collections import deque
from typing import List
class Solution:
    def bfs(self,i,j,grid,visited,rows,cols):
            visited[i][j] = 1
            queue = deque()
            queue.append((i,j))

            while queue:
                i,j = queue.popleft()
                for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    new_i,new_j = i+x,j+y
                    if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                        continue
                    if grid[new_i][new_j] == "0":
                        continue
                    if visited[new_i][new_j]==1:
                        continue
                    queue.append((new_i,new_j))
                    visited[new_i][new_j]=1

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                        count+=1
                        self.bfs(r,c,grid,visited,rows,cols)
                        
        return count

        

        
            

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
print(Solution().numIslands(grid2))
print(Solution().numIslands(grid1))
