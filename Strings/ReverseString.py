#Reverse a given string word wise. 
def reverseStringWordWise(string):
    new_li = string.split()
    new_li = new_li[::-1]
    new_string = " ".join(new_li)
    return new_string
