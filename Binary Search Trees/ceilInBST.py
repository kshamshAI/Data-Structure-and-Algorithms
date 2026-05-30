''' Ceil in BST
Difficulty: Medium
Given a root binary search tree and an integer x , find the Ceil of x in the tree.
Ceil(x) is a number that is either equal to x or is immediately greater than x. If Ceil could not be found, return -1.
Examples:
Input: root = [5, 1, 7, N, 2, N, N, N, 3], x = 3
Output: 3
Explanation: We find 3 in BST, so ceil of 3 is 3.
Input: root = [10, 5, 11, 4, 7, N, N, N, N, N, 8], x = 6
Output: 7
Explanation: We find 7 in BST, so ceil of 6 is 7.
Constraints:
1  ≤ Number of nodes  ≤ 105
1  ≤ Value of nodes ≤ 105'''
# Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 

        
class Solution:
    def findCeil(self,root:Node, x:int) ->int:
        # code here
        temp = root
        ceil = -1
        while temp:
            if temp.data == x:
                return temp.data
            elif temp.data < x:
                temp = temp.right
                
            else:
                ceil = temp.data
                temp = temp.left
           
        return ceil

root = [5, 1, 7, None, 2, None, None, None, 3]
x = 3
print(Solution().findCeil(root,x))