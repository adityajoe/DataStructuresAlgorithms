# In this problem,we are given an array, we need to make the array non decreasing by making atmost one change. 
 

def isPossible(arr, n):
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            count += 1
            problem_index = i

    if count > 1:
        return False
    elif count == 0:
        return True
    else:
        if problem_index == 0 or problem_index == n-2:
            #only one change because 0th index doesn't have anything before it and last index doesn't have anything after. 
            return True    

        #if it is not 0th of n-1th element, then there are some cases we need to check. Either problem_index is the problem or
        #problem index + 1 is the problem. 
        #1. Make my problem_index = problem_index-1 or problem_index + 1; basically try to fit problem index between front and back elements. 
        #2. Make problem_index + 1 = problem_index or problem_index+2; basically try to fit problem index + 1 between front and back elements.
        if arr[problem_index-1] <= arr[problem_index+1]:
            return True
        if arr[problem_index] <= arr[problem_index+2]:
            return True
        return False        
