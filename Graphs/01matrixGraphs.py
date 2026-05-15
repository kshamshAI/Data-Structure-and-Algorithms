'''Leetcode 542. 01 Matrix
Solved
Medium
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two cells sharing a common edge is 1.
Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.'''
from copy import deepcopy
from collections import deque

class Solution:
    def updateMatrix(self, mat):
        grid = deepcopy(mat)
        row = len(grid)
        col = len(grid[0])
        visited =[[0 for _ in range(col)] for _ in range(row)]
        distance =  [[0 for _ in range(col)] for _ in range(row)]
        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append([r,c,0])
                    visited[r][c] = 1
        while queue:
            i,j,d= queue.popleft()
            distance[i][j] = d
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                new_i = i+x
                new_j = j+y
                if new_i < 0 or new_i >=row or new_j < 0 or new_j >= col:
                    continue
                if visited[new_i][new_j] == 1 :
                    continue
                queue.append([new_i,new_j,d+1])
                visited[new_i][new_j] = 1
        return distance 

mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix(mat))
