
# Given the root of a binary search tree and a value key. 
# Insert a new node with a value equal to key into the tree and return the root of the modified tree after inserting the value. 
# Note: All the nodes have distinct values in the BST and the new value to be inserted is not present in the BST.

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def insert(self, root, key):
        # code here
        if not root:
            root = Node(key)
            return root
        if root.data == key:
            return root
        elif key > root.data:
            if root.right:
                self.insert(root.right,key)
            else:
                new = Node(key)
                root.right = new
        elif key < root.data:
            if root.left:
                self.insert(root.left,key)
            else:
                new = Node(key)
                root.left = new                
            
        return root    
