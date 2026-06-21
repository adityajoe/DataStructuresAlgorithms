'''
    Your task is to remove duplicates from given 
    sorted linked list.
    
    Function Arguments: head (head of the given linked list) 
    Return Type: none, just remove the duplicates from the list.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    #code here
    curr = head
    prev = None
    while curr:
        if prev is not None:
            if prev.data == curr.data:
                prev.next = curr.next
                curr = curr.next
                
            else:
                prev = curr
                curr = curr.next
        else:        
            prev = curr
            curr = curr.next
        
