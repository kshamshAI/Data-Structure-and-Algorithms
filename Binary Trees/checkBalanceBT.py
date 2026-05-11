# Leetcode-110
'''110. Balanced Binary Tree
Solved
Easy
Given a binary tree, determine if it is height-balanced.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:
Input: root = []
Output: true
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def func(node):
            if node == None:
                return 0
            lh = func(node.left)
            if lh == -1:
                return -1
            rh = func(node.right)
            if rh == -1:
                return -1
            difference = abs(lh - rh)
            if difference > 1:
                return -1
            return max(lh,rh)+1
        h = func(root)
        if h == -1:
            return False
        else:
            return True