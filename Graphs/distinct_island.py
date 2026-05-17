'''Number of Distinct Islands
Difficulty: MediumAccuracy: 62.29%Submissions: 131K+Points: 4Average Time: 20m
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).

Example 1:

Input:
grid[][] = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
Output: 1
Explanation:
grid[][] = [[1, 1, 0, 0, 0], 
            [1, 1, 0, 0, 0], 
            [0, 0, 0, 1, 1], 
            [0, 0, 0, 1, 1]]
Same colored islands are equal. We have 2 equal islands, so we have only 1 distinct island.

Example 2:

Input:
grid[][] = [[1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]]
Output: 3
Explanation:
grid[][] = [[1, 1, 0, 1, 1], 
            [1, 0, 0, 0, 0], 
            [0, 0, 0, 0, 1], 
            [1, 1, 0, 1, 1]]
Same colored islands are equal.
We have 4 islands, but 2 of them
are equal, So we have 3 distinct islands.

Your Task: You don't need to read or print anything. Your task is to complete the function countDistinctIslands() which takes the grid as an input parameter and returns the total number of distinct islands.

Constraints:
1 ≤ n, m ≤ 500
grid[i][j] == 0 or grid[i][j] == 1'''

# ---------------------------------Solution-------------------------------------------------------
from collections import deque
from typing import List

class Solution:
    def bfs(self,r,c,grid,visited,rows,cols):
        visited[r][c]=1
        queue = deque()
        queue.append((r,c))
        base_r =r
        base_c=c
        shape = []
        while queue:
            i,j = queue.popleft()
            shape.append((i-base_r,j-base_c))
            for k,v in [[-1,0],[0,-1],[0,1],[1,0]]:
                new_i,new_j = i+k,j+v
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if grid[new_i][new_j]==0:
                    continue
                if visited[new_i][new_j] == 1:
                    continue
                queue.append((new_i,new_j))
                visited[new_i][new_j]=1
        
        return shape
            
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        my_set = set()
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c]==0:
                    shape=self.bfs(r,c,grid,visited,rows,cols)
                    my_set.add(tuple(shape))
        return len(my_set)
    
    #DFS APPROACH
    def dfs(self,r,c,base_r,base_c,grid,visited,rows,cols,shape):
        visited[r][c]=1
        shape.append((r-base_r,c-base_c))
        for k,v in [[-1,0],[0,-1],[0,1],[1,0]]:
            new_i,new_j = r+k,c+v
            if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                continue
            if grid[new_i][new_j]==0:
                continue
            if visited[new_i][new_j] == 1:
                    continue
            self.dfs(new_i,new_j,base_r,base_c,grid,visited,rows,cols,shape)
        
        return shape
            
    def countDistinctIslands2(self, grid : List[List[int]]) -> int:
        # code here
        my_set = set()
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c]==0:
                    shape=[]
                    base_r =r
                    base_c=c
                    shape=self.dfs(r,c,base_r,base_c,grid,visited,rows,cols,shape)
                    my_set.add(tuple(shape))
        return len(my_set)
        


grid1 = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]

grid2 =  [[1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]]
Output: 3
print(Solution().countDistinctIslands2(grid1))
print(Solution().countDistinctIslands2(grid2))
