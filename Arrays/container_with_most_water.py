# Container with Most Water
# Given an array arr[] of non-negative integers, where each element arr[i] represents the height of the vertical lines, find the maximum amount of water that can be contained between any two lines, together with the x-axis.

class Solution:
    def maxWater(self, arr):
        # code here
        low = 0
        high = len(arr) - 1
        max_area = 0
        while low < high:
            base_area = high - low
            total_area = min(arr[high], arr[low]) * base_area
            # print(high, low)
            if total_area > max_area:
                max_area = total_area
            if arr[high] < arr[low]:
                high -= 1
            else:
                low +=1
        return max_area  
        
