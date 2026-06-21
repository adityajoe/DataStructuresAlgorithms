# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
# Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        d = dict(Counter(a))
        d2 = dict(Counter(b))
        if d == d2:
            return True
        else:
            return False
