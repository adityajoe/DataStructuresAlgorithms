# Given a string s, repeatedly remove all adjacent duplicate character pairs until no such pairs remain.
# Return the resulting string, or "-1" if the string becomes empty.

class Solution:
    def removePair(self,s):
        # code here
        li = []
        for char in s:
            if len(li) == 0:
                li.append(char)
                continue
            if char == li[-1]:
                li.pop()
            else:
                li.append(char)
        new = ''.join(li)
        if new == "":
            return "Empty String"
        return new        
