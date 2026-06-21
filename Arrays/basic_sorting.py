#Insertion Sort
class Solution:
    def insertionSort(self, arr):
        # code here
        for i in range(1, len(arr)):
            j = i-1
            key = arr[i]
            while j >= 0 and arr[j] >= key:
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = key

#Bubble Sort
class Solution:
    def bubbleSort(self,arr):
        # code here
        for j in range(len(arr)-1, -1, -1):
            for i in range(0,j):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1], arr[i]


#Selection Sort
class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            min_ele = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_ele]:
                    min_ele =  j
            arr[i],arr[min_ele] = arr[min_ele],arr[i]
