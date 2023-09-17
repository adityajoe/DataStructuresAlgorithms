#Question: You are given an array of Length N, Your task is to find the first missing positive integer in linear time. O(n)

#Brute Force Approach: In this approach I have sorted the array and started from 1. if 1 is found in the array, My first missing becomes 2 etc. 
def firstMissingBrute(arr, n):
    arr.sort()
    first_missing = 1
    for i in range(n):
        if arr[i] == first_missing:
            first_missing +=1
    return first_missing        

#Better Approach
def firstMissing(arr,n):
    visited=[False for i in range(n+2)]
    for i in arr:
        if i > 0 and i <= n:
            visited[i]= True
    for i in range(1, len(visited)):
        if visited[i] == False:
            return i     

