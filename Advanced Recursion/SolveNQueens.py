# Leetcode Problem 51(Hard Level)
'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:
Input: n = 1
Output: [["Q"]]
Constraints:
1 <= n <= 9'''
from typing import List

class Solution:
     #Brute Force Approach TC=O(N!*N),Space Complexity=O(N**2)-Backtracking
    def backtrack1(self,col,board,n,result):
        if col == n:
            result.append(list(board))
            return

        for row in range(n):
            if self.isSafe(row ,col,n,board):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.backtrack1(col+1,board,n,result)
                board[row] = board[row][:col] + "." + board[row][col+1:]
        return result

    def isSafe(self,row,col,n,board):
        # Left Horizontal
        duprow = row
        dupcol = col
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col-=1
        # left Upper Diagonal
        duprow = row
        dupcol = col
        while row >=0 and col >= n:
            if board[row][col] == "Q":
                return False
            row-=1
            col1=1
        # Left Lower Diagonal
        duprow = row
        dupcol = col

        while row <n and col >= 0:
            if board[row][col] == "Q":
                return False
            row+=1
            col-=1
        return True  
    def solveNQueens1(self, n: int) -> List[List[str]]:
        result = []
        col = n
        board = [["."]*n for _ in range(n)] 
        return self.backtrack1(0,board,n,result)  
    
    #Optimal Approach-Time Complexity=O(N!)(Backtracking+Hashing)
    def backtrack2(self,col,n,board,left_horizontal,left_upper_diagonal,left_lower_diagonal,result):
        if col == n:
            result.append(list(board))
            return
        for row in range(n):
            if (left_horizontal[row] == 0 and
                left_upper_diagonal[n-1+(col-row)] == 0 and
                left_lower_diagonal[row+col] == 0):
                    board[row] = board[row][:col] + "Q" + board[row][col+1:]
                    left_horizontal[row] = 1 
                    left_upper_diagonal[n-1+(col-row)] = 1 
                    left_lower_diagonal[row+col] = 1
                    self.backtrack2(col+1,n,board,left_horizontal,left_upper_diagonal,left_lower_diagonal,result)
                    board[row] = board[row][:col] + "." + board[row][col+1:]
                    left_horizontal[row] = 0
                    left_upper_diagonal[n-1+(col-row)] = 0 
                    left_lower_diagonal[row+col] = 0
        return result

    def solveNQueens2(self,n:int) -> List[List[str]]:
        result = []
        col = n
        board = ["."*n for _ in range(n)] 
        left_horizontal = [0]*n
        left_upper_diagonal = [0]*(2*n-1)
        left_lower_diagonal = [0]*(2*n-1)
        return self.backtrack2(0,n,board,left_horizontal,left_upper_diagonal,left_lower_diagonal,result)


print(Solution().solveNQueens2(4))