'''GFG Problem-----------------------Predecessor and Successor
Difficulty: Medium
You are given the root of a BST and an integer key. You need to find the inorder predecessor and successor of the given key. If either predecessor or successor is not found, then set it to NULL.

Note: In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 

Examples :

Input: root = [50, 30, 70, 20, 40, 60, 80], key = 65

Output: [60, 70]
Explanation: In the given BST the inorder predecessor of 65 is 60 and inorder successor of 65 is 70.
'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
 
    def dfs(self,node,predecessor,successor,key):
        if node == None:
            return predecessor,successor
        if node.val < key: 
            predecessor = node
            return self.dfs(node.right,predecessor,successor,key)

        if node.val > key:
            successor = node
            return self.dfs(node.left,predecessor,successor,key)
        
        return predecessor,successor
    
    # Inorder Traversal
    def solve(self,node,result):
        if node == None:
            return 
        
        left = self.solve(node.left,result)
        result.append(node.val)
        right = self.solve(node.right,result)
        
        return result
        
    # finding predecessor and successor using while loop
    def findPreSuc(self, root, key):
        temp = root
        predecessor = None
        successor = None
        while temp:
            if temp.data < key:
                predecessor = temp
                temp = temp.right
            else:
                temp = temp.left
        curr = root
        while curr:
            if curr.data > key:
                successor= curr
                curr = curr.left
            else:
                curr = curr.right
        return predecessor,successor 

    def findPreSucBST(self, root, key):
        current = root
        result = []
        predecessor = None
        successor = None
        while current:
            if current.left is None:
                if current.data < key:
                    predecessor = current
                elif current.data > key and successor is None: 
                    successor = current
                current = current.right
            else:
                prev = current.left
                while prev.right is not None and prev.right != current:
                    prev = prev.right
            if prev.right is None:
                prev.right = current
                current = current.left
            else:
                prev.right = None
                if current.data < key:
                    predecessor = current
                elif current.data > key and successor is None: 
                    successor = current
                current = current.right
                
        return predecessor,successor


        





n1  = TreeNode(20)
n2  = TreeNode(30)
n3  = TreeNode(40)
n4  = TreeNode(50)
n5  = TreeNode(60)
n6 = TreeNode(70)
n7 = TreeNode(80)


n4.left = n2
n2.left = n1
n2.right = n3
n4.right = n6
n6.left = n5
n6.right = n7
print(Solution().dfs(n4,None,None,65))
print(Solution().solve(n4,result=[]))