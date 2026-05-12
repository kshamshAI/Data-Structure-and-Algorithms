'''GeeksforGeeks Practice Problem------------
Top View of Binary Tree
Difficulty: MediumAccuracy: 38.43%Submissions: 457K+Points: 4Average Time: 45m
You are given the root of a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Note:
Return the nodes from the leftmost node to the rightmost node.
If multiple nodes overlap at the same horizontal position, only the topmost (closest to the root) node is included in the view. 
Examples:
Input: root = [1, 2, 3]
Output: [2, 1, 3]
Explanation: The Green colored nodes represents the top view in the below Binary tree.
Input: root = [10, 20, 30, 40, 60, 90, 100]
Output: [40, 20, 10, 30, 100]
Explanation: The Green colored nodes represents the top view in the below Binary tree.
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105'''
from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
        # Recursive approach(DFS)
        def func(self,node,line,level,dict):
            if node == None:
                return
            if line not in dict or level < dict[line][1]: 
                dict[line] = (node.data,level)
            self.func(node.left,line-1,level+1,dict)
            self.func(node.right,line+1,level+1,dict)


        def topView(self, root:Node):
            result = []
            dict = {}  
            self.func(root,0,0,dict)  
            for line in sorted(dict.keys()):
                result.append(dict[line][0])   
            return result

        # BFS Approach(Level order)
        

        def topView(self, root):
        # code here
            ans = []
            result = {}
            queue = deque([])
            if not root:
                return []
            queue.append((root,0))
            while queue:
                e,line = queue.popleft()
                if line not in result:
                    result[line] = e.data
                if e.left:
                    queue.append((e.left,line-1))
                if e.right:
                    queue.append((e.right,line+1))
            for line in sorted(result.keys()):
                ans.append(result[line])
            return ans
            
            
            
        