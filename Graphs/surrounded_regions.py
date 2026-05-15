'''Leetcode--130. Surrounded Regions----------------------
Solved
Medium
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
Example 2:
Input: board = [["X"]]
Output: [["X"]]
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.'''

##################Time Complexity=O(r*c)+O(2(r+c)), Space Complexity=O(r*c)+(O(r*c)-Stack space)

from typing import List
class Solution:
    def dfs(self,r,c,rows,cols,board,visited):
        if r<0 or r>=rows or c<0 or c>=cols:
            return
        if board[r][c] == 'X':
            return
        if visited[r][c] == 1:
            return
        visited[r][c] = 1
        self.dfs(r-1,c,rows,cols,board,visited)
        self.dfs(r,c-1,rows,cols,board,visited)
        self.dfs(r,c+1,rows,cols,board,visited)
        self.dfs(r+1,c,rows,cols,board,visited)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        # For First row(boundary)
        r = 0
        c = 0
        for c in range(cols):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,board,visited)
        # For Last row(boundary)
        r = rows-1
        c=0
        for c in range(cols):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,board,visited)
        # For First column(bounadry)
        r = 0
        c = 0 
        for r in range(rows):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,board,visited)
        # For Last column(boundary)
        r = 0
        c = cols-1
        for r in range(rows):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r,c,rows,cols,board,visited)
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and board[r][c]=='O':
                    board[r][c] = "X"
        return board
        
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(f'Output :{Solution().solve(board)}')