'''Leetcode 104. Maximum Depth of Binary Tree
Solved
Easy
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2
Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100'''

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    #Recursive Approach
    def func(self,node):
        if node == None:
            return 0
        lh = self.func(node.left)
        rh = self.func(node.right)
        return 1+max(lh,rh)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.func(root)

    # iterative Approach
    def max_depth(self,root:Optional[TreeNode]) -> int:
        queue = [] #dequeue
        height = 0
        while len(queue) != 0:
            level_size = len(queue)
            height += 1
        queue.append(root.val)
        for _ in range(level_size):
            e = queue.popleft()
            if e.left != None:
                queue.append(e.left)
            if e.right != None:
                queue.append(e.right)
        return height

