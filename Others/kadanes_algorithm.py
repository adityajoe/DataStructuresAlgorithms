# You are given an integer array arr[].
# You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        global_max = -1000000
        pre_ele_max = -100000000
        for i in range(len(arr)):
            if i == 0:
                global_max = arr[0]
                pre_ele_max = arr[0]
            else:
                pre_ele_max = max(pre_ele_max + arr[i], arr[i])
                global_max = max(global_max, pre_ele_max)
        return global_max        
