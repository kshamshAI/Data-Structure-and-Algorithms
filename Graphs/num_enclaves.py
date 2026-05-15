'''Leetcode---1020. Number of Enclaves-------------------------------------------------------------
Solved
Medium
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.'''
##################Time Complexity=O(r*c)+O(2(r+c)), Space Complexity=O(r*c)+(O(r*c)-Stack space)

from typing import List
from collections import deque

class Solution:
    def dfs(self,r,c,rows,cols,grid,visited):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if grid[r][c] == 0:
            return
        if visited[r][c] == 1:
            return
        visited[r][c] = 1
        self.dfs(r-1,c,rows,cols,grid,visited)
        self.dfs(r,c-1,rows,cols,grid,visited)
        self.dfs(r,c+1,rows,cols,grid,visited)
        self.dfs(r+1,c,rows,cols,grid,visited)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Do not return anything, modify grid in-place instead."""
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        # For First row(boundary)
        r = 0
        c = 0
        for c in range(cols):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,grid,visited)
        # For Last row(boundary)
        r = rows-1
        c=0
        for c in range(cols):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,grid,visited)
        # For First column(bounadry)
        r = 0
        c = 0 
        for r in range(rows):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,grid,visited)
        # For Last column(boundary)
        r = 0
        c = cols-1 
        for r in range(rows):
            if grid[r][c] == 1:
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,grid,visited)


        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c]==1:
                    count+=1
        return count
    
    #BFS
    def numEnclaves1(self, grid: List[List[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
    
            # For First row(boundary)
        r = 0
        c = 0
        for c in range(cols):
            if grid[r][c] == 1:
                    queue.append((r,c))
                    visited[r][c] = 1
        # For Last row(boundary)
        r = rows-1
        c=0
        for c in range(cols):
            if grid[r][c] == 1:
                    queue.append((r,c))
                    visited[r][c] = 1
        # For First column(bounadry)
        r = 0
        c = 0 
        for r in range(rows):
            if grid[r][c] == 1:
                    queue.append((r,c))
                    visited[r][c] = 1
        # For Last column(boundary)
        r = 0
        c = cols-1
        for r in range(rows):
            if grid[r][c] == 1:
                    queue.append((r,c))
                    visited[r][c] = 1
        while queue:
            i,j = queue.popleft()
            for x,y in [(1,0),(-1,0),(0,-1),(0,1)]:
                new_i = i + x
                new_j = j + y
                if new_i < 0 or new_i>=rows or new_j <0 or new_j>=cols:
                    continue
                if grid[new_i][new_j] == 0:
                    continue
                if visited[new_i][new_j] == 1 and grid[new_i][new_j] == 1:
                    continue 
                queue.append((new_i,new_j))
                visited[new_i][new_j]=1


        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c]==1:
                    count+=1
        return count
                        
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(Solution().numEnclaves1(grid))
