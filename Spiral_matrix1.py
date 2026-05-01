#Leetcode Problem--54
'''Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100'''

# Single Solution----Time Complexity=O(m*n)
def spiral_matrix(matrix):
        result = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        left = 0
        right = n-1
        bottom = m-1
        while (top<=bottom) and (left<=right):
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1


            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1


            if top <= bottom:    # For edge case(single row)
                   
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1


            if left<= right:    # For edge case(single column)
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1

        return result


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
(print(spiral_matrix(matrix)))