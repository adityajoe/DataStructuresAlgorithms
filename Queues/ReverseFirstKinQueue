# Given an integer k and a queue of integers, we need to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.

# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.

import collections
class Solution:
    def reverseFirstK(self, q, k):
        if k> len(q) or k == 0:
            return q
        #code here
        arr = []
        q2 = collections.deque()
        count = 0
        while count <k:
            count +=1
            arr.append(q.popleft())
            # print(arr)
        while arr:
            q.append(arr.pop())
        count = 0
        while count < len(q) - k:
            count += 1
            q.append(q.popleft())
        return q   
