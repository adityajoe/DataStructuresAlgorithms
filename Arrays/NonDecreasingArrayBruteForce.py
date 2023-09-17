
#You are given an array, we need to check if the array can be made non decreasing by making atmost one change. 

#Checks if the array is non decreasing
def isNonDecreasing(arr,n):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

#Checks if it is possible to make the array non decreasing
def isPossible(arr, n):
    for i in range(n):
        oldVal = arr[i]
        if(i > 0):
            arr[i] = arr[i - 1]
        else:
            arr[i] = float('-inf')
        if(isNonDecreasing(arr, n)):
            return True
        arr[i] = oldVal
    return False


