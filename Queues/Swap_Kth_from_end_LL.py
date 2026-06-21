# Given the head of a singly linked list and an integer k. Swap the kth node (1-based index) from the beginning and the kth node from the end of the linked list. Return the head of the final formed list and if it's not possible to swap the nodes return the original list.




'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length +=1
        if k > length:
            return head
        k_end = length - k +1
        if k_end == k:
            return head
        curr = head
        count = 0
        
        while curr is not None:
            count+=1
            if count == k:
                start_node = curr
            elif count == k_end:
                end_node = curr
            curr = curr.next    
        start_node.data,end_node.data = end_node.data,start_node.data      
        return head
            
        
        
