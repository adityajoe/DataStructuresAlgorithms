Implement a class SpecialStack that supports following operations:

push(x) – Insert an integer x into the stack.
pop() – Remove the top element from the stack.
peek() – Return the top element from the stack. If the stack is empty, return -1.
getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
isEmpty() –  Return true if stack is empty, else false
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call push(x)
2:  Call pop()
3: Call peek()
4: Call getMin()
5: Call isEmpty()
The driver code will process the queries, call the corresponding functions, and print the outputs of peek(), getMin(), isEmpty() operations.
You only need to implement the above five functions.

class Solution:

    def __init__(self):
        # code here
        self.stack = []
        self.min_stack = []
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
                    
    # Remove the top element from the Stack
    def pop(self):
        if self.min_stack:
            self.min_stack.pop()
        if self.stack:
            return self.stack.pop()
        else:
            return -1


    # Returns top element of Stack
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
    
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1


    # Finds minimum element of Stack
    def getMinbrute(self):
        if self.stack:
            copy = sorted(self.stack)
            return copy[0]
        else:
            return -1
