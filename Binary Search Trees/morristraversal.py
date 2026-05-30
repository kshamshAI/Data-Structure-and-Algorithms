'''Traversal in binary tree using **********Morris Traversal Algorithm***********:
ordinary inorder traversal using DFS takes time complexity as O(n) as well as space complexity as O(n) being stack space,n= number of nodes
whereas morris traversal algo traverse in optimized space complexity of O(1) using temporary threaded connection'''

from typing import Optional
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def InorderMorris(self,root:Optional[TreeNode]):
        current = root
        result = []
        
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                        predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right
        return result
    
    def PreorderMorris(self,root:Optional[TreeNode]):
        current = root
        result = []
        
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                        predecessor = predecessor.right
                if predecessor.right is None:
                    result.append(current.val)
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right
        return result
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)


n1.left = n2
n2.left = n3
n2.right = n4
n2.right = n4
n4.right = n5
n5.right = n6
n1.right = n7
n7.left = n8
n7.right = n9
print(Solution().InorderMorris(n1))
print(Solution().PreorderMorris(n1))

            

