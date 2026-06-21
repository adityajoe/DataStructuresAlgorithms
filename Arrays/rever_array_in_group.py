#Reverse array in Groups

class Solution:
    # Function to reverse every sub-array group of size k.
    def reverse(self, arr,si,ei):
        while si<ei:
            arr[si],arr[ei] = arr[ei],arr[si]
            si += 1
            ei -= 1
    def reverseInGroups(self, arr, k):
        l = len(arr)
        if k > l:
            self.reverse(arr, 0, l-1)
        else:
            for i in range(0,l,k):
                si = i
                ei = min(si+k-1,l-1)
                self.reverse(arr,si,ei)
        

                
                

        

                
                
