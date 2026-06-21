# Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. 
Determine whether the Expression is balanced or not.
# An expression is balanced if:
# Each opening bracket has a corresponding closing bracket of the same type.
# Opening brackets must be closed in the correct order.

class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        if len(s) % 2 == 1:
            return False
        for bracket in s:
            if bracket in ['[', '{', '(']:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if bracket == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(bracket)
                elif bracket == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(bracket)
                elif bracket == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(bracket)
            
        if len(stack) == 0:
            return True
        else:
            return False
        
        
