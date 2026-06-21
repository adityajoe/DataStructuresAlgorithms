'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:

    def find_length(self, head):
        count = 0
        pointer = head
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count    
    
    def reverseList(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        prev = None
        curr = head
        flag = True
        while flag:
            next = curr.next
            curr.next = prev
            prev = curr
            if next is not None:
                curr = next
            else:
                flag = False
        return curr
        
    def isPalindrome(self, head):
        # code here
        if head.next is None or head is None:
            return True
            
        length = self.find_length(head)
        first_index = length//2
        if length % 2 == 0:
            diff = 1
        else:
            diff = 2
        pointer = head   
        count = 0
        while pointer is not None:
            count +=1
            if count == first_index:
                if diff == 1:
                    second_head = pointer.next
                    pointer.next = None
                else:
                    second_head = pointer.next.next
                    pointer.next = None
                break
            pointer = pointer.next
        second_head = self.reverseList(second_head)
        pointer = head
        pointer2 = second_head
        while pointer is not None and pointer2 is not None: 
            # print(pointer.data)
            # print(pointer2.data)
            if pointer.data != pointer2.data:
                break
            pointer = pointer.next
            pointer2 = pointer2.next
        else:
            return True
        return False    
        
        
        
