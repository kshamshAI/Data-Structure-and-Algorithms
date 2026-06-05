'''Leetcode----------------------------------235. Lowest Common Ancestor of a Binary Search Tree
Solved
Medium
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2'''
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    # Approach 1(for BT or BST)
    def dfs(self,node,p,q):
        if node is None:
            return None
        if node == p:
            return node
        if node == q:
            return node
        left = self.dfs(node.left,p,q)
        right = self.dfs(node.right,p,q)
        if left == None and right == None:
            return  None
        elif left == None:
            return right
        elif right == None:
            return left
        return node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q) 
    
class Solution2:
    # Approach 2(For BST)
    def dfs(self,node,p,q):
        if node is None:
            return None
        if node.val < p.val and node.val < q.val:
            return self.dfs(node.right,p,q) 
        if node.val > p.val and node.val > q.val:
            return self.dfs(node.left,p,q) 
        
        return node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q) 

class Solution3:
    # Approach 3(For BST)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while True:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif curr == p:
                return p
            elif curr == q:
                return q
            else:
                return curr