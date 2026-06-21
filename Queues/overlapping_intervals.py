# Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

class Solution:
    def mergeOverlap(self, arr):
        # Code here
        arr.sort()
        interval_stack = [arr[0]]
        for i in range(1, len(arr)):
            if interval_stack[-1][-1] >= arr[i][0]:
                interval_stack[-1] = [interval_stack[-1][0], max(interval_stack[-1][1], 
                arr[i][1])]
            else:
                interval_stack.append(arr[i])
        return interval_stack        
                
        
