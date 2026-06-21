class Solution:
    def findEquilibrium(self, arr):
        # code here
        s = sum(arr)
        l_sum = 0
        r_sum = 0
        for i in range(len(arr)-1):
            l_sum = l_sum + arr[i]
            r_sum = s - l_sum - arr[i+1]
            if l_sum == r_sum:
                return i+1
        return -1        
