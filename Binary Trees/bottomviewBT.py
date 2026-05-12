'''GeeksforGeeks Practice Problem
Bottom View of Binary Tree
Difficulty: Medium
You are given the root of a binary tree, and your task is to return its bottom view. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level order traversal is considered.
Examples :
Input: root = [1, 2, 3, 4, 5, N, 6]
Output: [4, 2, 5, 3, 6]
Explanation: The Green nodes represent the bottom view of below binary tree.
Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
Output: [5, 10, 4, 28, 25]
Explanation: The Green nodes represent the bottom view of below binary tree.
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105'''
from collections import deque
#Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Solution:
    def bottomView(self, root):
        # code here
                # code here
        ans = []
        result = {}
        queue = deque([])
        if not root:
            return []
        queue.append((root,0))
        while queue:
            e,line = queue.popleft()
            
            result[line] = e.data
            if e.left:
                queue.append((e.left,line-1))
            if e.right:
                queue.append((e.right,line+1))
        for line in sorted(result.keys()):
            ans.append(result[line])
        return ans
        