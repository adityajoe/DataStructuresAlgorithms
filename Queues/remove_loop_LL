
'''
# node class:
# Given the head of a singly linked list, the task is to remove a cycle if present. A cycle exists when a node's next pointer points back to a previous node, forming a loop.

# Internally, a variable pos is used to denotes the position of the node where the cycle starts, but it is not passed as a parameter.
# The linked list remains as it is if there is cycle in the list.
# The output will be "true" if your code works according to expectations, otherwise "false". 


class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:

    def removeLoop(self, head):
        # code here
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return 0
        
        slow = head
        while slow!= fast:
            slow = slow.next
            fast = fast.next
        loop_start = slow
        ptr_next = loop_start
        while ptr_next.next != loop_start:
            ptr_next = ptr_next.next
        ptr_next.next = None
        return head
            
