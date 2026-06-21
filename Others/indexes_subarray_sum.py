# Given an array arr[] containing only non-negative integers, 
# your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. 
# You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. 
# You need to find the first subarray whose sum is equal to the target.

#User function Template for python3
class Solution:
    def find_sum(self, arr, si,ei):
        # print(si,ei)
        if si <= ei and ei < len(arr):
            sum = 0
            for i in range(si,ei+1):
                sum += arr[i]
            return sum
        else:
            return -1
    
    def subArraySum(self, arr, target):
        # code here
        si = 0
        ei = 0
        sum = self.find_sum(arr,si,ei)
        flag = True
        while flag:
            # print(si,ei)
            if ei >= len(arr) or sum == -1:
                flag = False
                continue
            if sum < target:
                ei+=1
                sum = self.find_sum(arr,si,ei)
            elif sum > target:
                si += 1
                if ei< si:
                    ei = si
                sum = self.find_sum(arr,si,ei)
            else:
                return [si+1, ei+1]
            
        else:
            return [-1]
            
