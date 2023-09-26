#Question: Given a string pattern which contrains only two types of characters '(', ')'. 
#Find the minimum number of paranthesis we must add to the string pattern so that our string is valid.access
#My approach: Find open left brackets and right brackets and add them both. we cut out open left brackets when we find open right brackets corresponding to them. 


def minimumParentheses(pattern):
    prev_bracket = -1
    curr_bracket = -1
    open_l = 0
    open_r = 0
    for char in pattern:
        if char == '(':
            curr_bracket = 'lb'
            open_l +=1
            prev_bracket = 'lb'
        else:
            curr_bracket = 'rb'
            if prev_bracket == -1 or prev_bracket == 'rb':
                if open_l == 0:
                    open_r += 1
                else:
                    open_l -=1  
            else:
                open_l -=1      
            prev_bracket = 'rb'
    return open_l + open_r              

