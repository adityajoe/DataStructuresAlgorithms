# Search a node in BST

class BST:
    def search(self, node, x):
        #code here
        call1, call2 = False, False
        if node == None:
            return False
        if node.data == x:
            return True
        elif node.data < x:
            call1 = self.search(node.right, x)
        elif node.data > x:
            call2 = self.search(node.left, x)
        return call1 or call2    
