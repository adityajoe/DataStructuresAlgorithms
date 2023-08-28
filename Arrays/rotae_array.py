#Problem Statement: Given an array arrwith n elements, the task is to rtate the array to the left by k steps 
#where k is non-negative.


#Your code goes here.
def rotate_array(arr, k): 
    #Space complexity: O(N), time complexity: O(N)
    new_arr = [0]*len(arr)
    for i in range(len(arr)):
        new_index = i-k
        new_arr[new_index] = arr[i]
    return new_arr 

def rotate_array2(arr,k):
    #space complexity : 0 , time complexity: O(N*K)
    for i in range(k):
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr)-1] = temp
    return arr            



n = int(input())
li = [int(i) for i in input().split()]
k = int(input())
result = rotate_array2(li, k)
for i in result:
    print(i, end = " ")



























