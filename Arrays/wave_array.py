class Solution:
    def sortInWave(self, arr):
        # code here
        if len(arr) == 1:
            return
        
        i = 0
        while i < len(arr)-1:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i = i+2
            
        
