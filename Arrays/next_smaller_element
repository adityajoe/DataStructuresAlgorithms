class Solution:
    def nextSmallerEle(self, arr):
        # code here
        stack = [arr[-1]]
        nse = [-1]
        for i in range(len(arr)-2, -1, -1):
          #  print(stack)
          #  print(nse)
            if arr[i] > stack[-1]:
                nse.append(stack[-1])
                stack.append(arr[i])
            else:
                while len(stack) > 0 and arr[i] <= stack[-1]:
                    stack.pop()
                if len(stack) == 0:
                   nse.append(-1)
                else:
                    nse.append(stack[-1])
                stack.append(arr[i])
        return nse[::-1]        
