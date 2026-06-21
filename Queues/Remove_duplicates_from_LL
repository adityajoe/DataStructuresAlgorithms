# Given a head of an unsorted linked list. Remove duplicate elements from this unsorted Linked List. 
# When a value appears in multiple nodes, the node which appeared first should be kept, all other duplicates are to be removed


'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
    
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        dic = {}
        prev =  None
        pointer = head
        while pointer is not None:
            if pointer.data not in dic:
                dic[pointer.data] = 1
                prev = pointer
                pointer = pointer.next
            else:
                if pointer == head:
                    head = head.next
                    pointer = head

                else:
                    prev.next = pointer.next
                    pointer = pointer.next
        return head
                
