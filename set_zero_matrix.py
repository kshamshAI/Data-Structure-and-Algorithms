# Leetcode Problem-73--Set zeros
'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1'''
 
#Brute force solution----Time Complexity-O((r+c)(r*c)+(r*c))------Space Complexity-O(1)
def mark_infinity(matrix,row,col):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0,r):
        if matrix[i][col] != 0:
             matrix[i][col] = float('inf')
    for j in range(0,c):
        if matrix[row][j] != 0:
             matrix[row][j]= float('inf')

def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j] == 0:
                mark_infinity(matrix,i,j)
    for i in range(0,rows):
        for j in range(0,cols):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = 0
    return matrix


# Optimal Approach
def set_zeros2(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    row_track = [0 for _ in range(row)]
    col_track = [0 for _ in range(cols)]
    for i in range(0,row):
        for j in range(0,cols):
            if matrix[i][j] == 0:
                row_track[i] = -1
                col_track[j] = -1
    for i in range(0,row):
        for j in range(0,cols):   
            if row_track[i] == -1 or col_track[j] == -1:
                matrix[i][j] = 0   
    return matrix

    

        
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
new_matrix = set_zeros2(matrix)
print(new_matrix)