"""  list Node is as defined below:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        # code here
        curr = head
        # print(curr.data)
        while curr.next is not None:
            next = curr.next
            curr.data,next.data = next.data, curr.data
            if next.next is not None:
                curr = next.next
            else:
                break
        curr = head
        while curr is not None:
            print(curr.data, end = " ")
            curr = curr.next
