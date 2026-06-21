# Given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. 
# A single person can perform only one activity at a time, meaning no two activities can overlap. 
# Your task is to determine the maximum number of activities that a person can complete in a day.
# Note: Start time and finish time cannot overlap, i.e., if a person finishes an activity at time x, then they cannot start another activity at time x.


class Solution:
    def querySum(self, n, arr, q, queries):
        # code here
        presum_arr = []
        postsum_arr = []
        query_sum = []
        for i in range(len(arr)):
            if i == 0:
                presum_arr.append(arr[0])
            else:
                presum_arr.append(presum_arr[-1] + arr[i])
        li = len(arr)-1             
        for i in range(li, -1, -1):
            if i == li:
                postsum_arr.append(arr[len(arr)-1])
            else:
                postsum_arr.append(postsum_arr[-1] + arr[i])
        
        postsum_arr = postsum_arr[::-1]
        
        for i in range(0, len(queries)-1, 2):
            si = queries[i] - 1
            ei = queries[i+1] - 1
            if si == 0:
                if ei == li:
                    query_sum.append(postsum_arr[0])
                else:
                    query_sum.append(presum_arr[ei])
            else:
                if ei == li:
                    query_sum.append(postsum_arr[si])
                else:
                    query_sum.append(postsum_arr[0] - presum_arr[si-1] - postsum_arr[ei+1])
                    
        return query_sum            
            
