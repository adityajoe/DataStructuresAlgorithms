# Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. 
# Return true/false depending upon whether there is a subarray present with 0-sum or not. 

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.

    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        sum_dict = {}
        sum = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                return True
            sum += arr[i]
            if sum == 0:
                return True
            if sum in sum_dict:
                return True
            else:
                sum_dict[sum] = 1
        return False
            
