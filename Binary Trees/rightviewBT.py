from collections import deque
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #BFS Approach
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque([])
        queue.append(root)
        while queue:
            level_size = len(queue)ADD
            for i in range(level_size):
                e = queue.popleft()
                if i == (level_size-1):
                    ans.append(e.val)
                if e.left!=None:
                    queue.append(e.left)
                if e.right!=None:
                    queue.append(e.right)
        return ans
    # Recursive Approach
    def func(self,node,level,result):
        if node == None:
            return
        if len(result) == level:
            result.append(node.val)
        if node.right:
            self.func(node.right,level+1,result)
        if node.left:
            self.func(node.left,level+1,result)
        return result



    def rightView(self,root:Optional[TreeNode]):

        return self.func(root,0,result=[])
