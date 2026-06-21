# Given two integer arrays a1[] and a2[]. 
# Sort the first array a1[] such that all the relative positions of the elements in the first array are the same as the elements in the second array a2[].
# Note: If elements are repeated in the second array, consider their first occurance only. 
# Elements not in a2[] should appear in a1[] at the end in ascending order.

#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    def sort_array(self, num):
        return (self.dic1.get(num, float('inf')), num)
        
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        self.dic1 = {}
        for i in range(len(A2)):
            self.dic1[A2[i]] = i
        # print(self.dic1)    
        # Your Code Here
        new = sorted(A1, key = self.sort_array)
        return new
    
