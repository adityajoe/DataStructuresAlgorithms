# Given an array arr[] with non-negative integers representing the height of blocks. 
# If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 


class Solution:
    def maxWater(self, arr):
        # code here
        total_water = 0
        l_max = []
        r_max = []
        for i in range(1, len(arr)-1):
            if i == 1:
                l_max.append(arr[0])
            else:
                l_max.append(max(l_max[-1], arr[i-1]))
        for i in range(len(arr)-2, 0, -1):
            if i == len(arr)-2:
                r_max.append(arr[len(arr)-1])
            else:    
                r_max.append(max(r_max[-1],arr[i+1]))
        r_max = r_max[::-1]
        # print(l_max)
        # print(r_max)
        for i in range(1, len(arr)-1):
            water = max(0, min(l_max[i-1], r_max[i-1]) - arr[i])
            total_water += water
        return total_water
        
        
