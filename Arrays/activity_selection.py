# Given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. 
# A single person can perform only one activity at a time, meaning no two activities can overlap. 
# Your task is to determine the maximum number of activities that a person can complete in a day.

# Note: Start time and finish time cannot overlap, i.e., if a person finishes an activity at time x, then they cannot start another activity at time x.


class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,finish):
        activities = []
        num_acts = 0
        for i in range(len(start)):
            activities.append([start[i], finish[i]])
            
        activities.sort(key = lambda x:x[1])
        # print(activities)
        for i in range(len(activities)):
            # print(num_acts)
            if num_acts == 0:
                prev = 0
                num_acts +=1
            else:
                if activities[i][0] > activities[prev][1]:
                    num_acts +=1
                    prev = i    
        return num_acts
                
