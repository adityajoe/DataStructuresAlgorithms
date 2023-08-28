#Write a function to find the second largest element in an array
def findSecondLargest(sequenceOfNumbers):
    second_largest = float('-inf')
    largest = sequenceOfNumbers[0]
    for i in range(1, len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] == largest: #Why do this? 
            continue
        if sequenceOfNumbers[i] > largest:
            second_largest = largest
            largest = sequenceOfNumbers[i]
        elif sequenceOfNumbers[i] > second_largest:
            second_largest = sequenceOfNumbers[i]
        else:
            continue 
    if second_largest == float('-inf'):       #Why do this?  
        return -1
    return second_largest                    

Learnin: Think About Boundary Cases
