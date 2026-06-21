# Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

# Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

class Solution:
    def majorityElement(self, arr):
        #code here
        cand_ele = -1
        votes = 0
        for i in range(len(arr)):
            if votes == 0:
                cand_ele = arr[i]
                votes = 1
            else:
                if arr[i] == cand_ele:
                    votes +=1
                else:
                    votes -=1
        count = 0
        for i in range(len(arr)):
            if arr[i] == cand_ele:
                count += 1
        if count > len(arr)//2:
            return cand_ele
        else:
            return -1
                
