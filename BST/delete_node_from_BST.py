

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    
    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root
    def deleteNode(self, root, x):
        #code here
        if not root:
            return None
        if x > root.data:
            root.right = self.deleteNode(root.right,x)
            return root
        elif x < root.data:
            root.left = self.deleteNode(root.left, x)
            return root
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
                
            min_value = self.findMin(root.right)
            root.data = min_value.data
            root.right = self.deleteNode(root.right, min_value.data)
            
            return root    
                
