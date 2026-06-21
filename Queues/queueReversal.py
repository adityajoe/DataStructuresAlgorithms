# Given a queue q containing integer elements, your task is to reverse the queue.

import collections
class Solution:
    def reverseQueue(self, q):
        # code here
        s2 = []
        while q:
            s2.append(q.popleft())
        # print(s2)    
        while s2:
            print(s2.pop(), end = " ")
        
