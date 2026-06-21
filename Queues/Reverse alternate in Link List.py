# Given a singly linked list, perform the following operations: extract all alternate nodes starting from the second node, reverse the extracted list, and append it at the end of the remaining list to obtain the final modified linked list.




"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

"""
class Solution:
    
    def create_linked_list(self, values):
        if not values:   # empty list
            return None
        
        head = Node(values[0])   # first node
        curr = head
        
        for val in values[1:]:   # build the rest
            curr.next = Node(val)
            curr = curr.next
        
        return head
        
    
    def reverseLinkedList(self, head):
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
    
    def rearrange(self, head):
        # Code here
        pointer = head
        alt_nodes = []
        while pointer is not None:
            if pointer.next is not None:
                alt_nodes.append(pointer.next.data)
                pointer.next = pointer.next.next
            
            pointer = pointer.next
        
        
        alt_head = self.create_linked_list(alt_nodes)
        reversed_head =  self.reverseLinkedList(alt_head)
        
        pointer = head
        while pointer.next is not None:
             pointer = pointer.next
        pointer.next = reversed_head
    
