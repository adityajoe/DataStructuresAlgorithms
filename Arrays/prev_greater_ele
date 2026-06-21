class Solution:
    def preGreaterEle(self, arr):
        # code here
        stack = [arr[0]]
        pge = [-1]
        for i in range(1, len(arr)):
            if arr[i] < stack[-1]:
                pge.append(stack[-1])
                stack.append(arr[i])
            else:
                while len(stack) > 0 and arr[i] >= stack[-1]:
                    stack.pop()
                if len(stack) == 0:
                    pge.append(-1)
                else:
                    pge.append(stack[-1])
                stack.append(arr[i]) 
        return pge    
        
