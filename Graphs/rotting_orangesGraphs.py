'''Leetcode 994. Rotting Oranges
Medium
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.'''

from copy import deepcopy
from typing import List
from collections import deque
class Solution:
    # BFS Approach only applicable
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) 
        matrix = deepcopy(grid)
        fresh_count = 0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 2:
                    queue.append((r,c))
            
                elif matrix[r][c] == 1:
                    fresh_count+=1
        minutes = 0
        while queue and fresh_count>0:
            minutes +=1
            rotten = len(queue)
            for _ in range(rotten):
                i,j = queue.popleft()
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    new_i = i + dx
                    new_j = j + dy
                    if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                        continue
                    elif matrix[new_i][new_j] == 0 or matrix[new_i][new_j] == 2:
                        continue
                    matrix[new_i][new_j] = 2
                    fresh_count-=1
                    queue.append((new_i,new_j))
        if fresh_count>0:
            return -1
        return minutes
grid =[[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))