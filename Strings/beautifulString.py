#Given a binary string contraining only 0 or 1. We need tom make it beautiful.
#A binary string is called beautiful if it contains alternating 0s and 1s.


def isbeautiful(string):
    prev = -1
    for char in string:
        if prev == -1:
            prev = char
            continue
        if char ==1 and prev == 0:
            prev = 1
        elif char == 0 and prev in 1:
            prev = 0    
        else:
            return False
    else:
        return True  

def make_beautiful_subs(l):
    b1 = ""
    b2 = ""
    for i in range(1, l+1):
        if i%2 == 0:
            b1 += "0"
            b2 += "1"
        else:
            b1 += "1"
            b2 += "0"    
    return b1,b2
        

def makeBeautiful(string):
    if isbeautiful(string):
        return 0
    l = len(string)
    str1,str2 = make_beautiful_subs(l)
    count1 = 0
    count2 = 0
    for i in range(len(string)):
        if string[i] != str1[i]:
            count1 +=1
        if string[i] != str2[i]:
            count2 += 1
    return min(count1,count2)            



