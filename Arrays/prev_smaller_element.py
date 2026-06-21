class Solution:
    def prevSmaller(self, arr):
        # code here
        stack = [arr[0]]
        pse = [-1]
        for i in range(1, len(arr)):
            if arr[i] > stack[-1]:
                pse.append(stack[-1])
                stack.append(arr[i])
            else:
                while len(stack) > 0 and arr[i] <= stack[-1]:
                    stack.pop()
                if len(stack) > 0:
                    pse.append(stack[-1])
                else:
                    pse.append(-1)
                stack.append(arr[i])
        return pse
