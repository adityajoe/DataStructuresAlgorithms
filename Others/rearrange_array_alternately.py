# Given an array of positive integers. Your task is to rearrange the array elements alternatively i.e. 
# first element should be the max value, the second should be the min value, the third should be the second max, the fourth should be the second min, and so on.
# Note: Modify the original array itself. Do it without using any extra space. You do not have to return anything.

#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self, arr, n): 
        ##Your code here
        new = []
        si = [i for i in range(0, n//2)]
        if n %2 == 0:
            li = [j for j in range(n//2,n)]
        else:
            li = [j for j in range(n//2 + 1,n)]
        li = li[::-1]
        
        # print(li)
        # print(si)
        
        for i in range(n//2):
            new.append(arr[li[i]])
            new.append(arr[si[i]])
        if n%2 != 0:
            new.append(arr[n//2])
        arr[:] = new
        # print(arr)
 
            
