

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        slow = head
        fast = head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            if fast is None or fast.next is None:
                return False
        return False        
        
