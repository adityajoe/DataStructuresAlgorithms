#Question: You are given an array of Length N, Your task is to find the first missing positive integer in linear time. O(n)

#Brute Force Approach: In this approach I have sorted the array and started from 1. if 1 is found in the array, My first missing becomes 2 etc. 

def firstMissing(arr, n):
    arr.sort()
    first_missing = 1
    for i in range(n):
        if arr[i] == first_missing:
            first_missing +=1
    return first_missing        

