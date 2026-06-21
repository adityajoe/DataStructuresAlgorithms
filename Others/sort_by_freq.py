# Given an array of integers arr[], sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. 
# If the frequencies of two elements are the same, then the smaller number comes first.

#User function Template for python3
import functools 

class Solution:
   
    #Function to sort the array according to frequency of elements.
    def comparator(self,a,b):
        if a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        if a[0] < b[0]:
          return -1
        elif a[0] > b[0]:
            return 1
        else:
            return 0
        
    
    
    def sortByFreq(self,a,n):
        dict = {}
        new = []
        for i in a:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        # print(dict.items())
        sorted_items = sorted(dict.items(), key=functools.cmp_to_key(self.comparator))
        
        for item in sorted_items:
          for v in range(item[1]):
            new.append(item[0])
        return new

