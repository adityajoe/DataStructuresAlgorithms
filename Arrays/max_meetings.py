# Given two arrays s[] and f[], where s[i] denotes the start time and f[i] denotes the finish time of the i-th meeting. 
# There is only one meeting room, find the maximum number of meetings that can be scheduled in the room such that no two selected meetings overlap in time. 
# Return the indices(1-based) of the selected meetings in sorted (increasing) order.




from typing import List


class Solution:
    def maxMeetings(self, N : int, start : List[int], finish : List[int]) -> List[int]:
        activities = []
        num_acts = []
        for i in range(len(start)):
            activities.append([start[i], finish[i], i])
            
        activities.sort(key = lambda x:x[1])
        # print(activities)
        for i in range(len(activities)):
            # print(num_acts)
            if len(num_acts) == 0:
                prev = 0
                num_acts.append(activities[i][2]+1)
            else:
                if activities[i][0] > activities[prev][1]:
                    num_acts.append(activities[i][2]+1)
                    prev = i    
        num_acts.sort()
        return num_acts
        
