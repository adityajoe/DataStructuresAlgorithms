#You are given a text message, we need to encode the text: the basic idea is to represent repeated successive characters as the character and single count
#Eg: aabbc --> a2b2c1 

def encode(message):
    prev_char = -1
    cuurent_char = -1
    output_message = ""
    count = 0
    for char in message:
        current_char = char
        if prev_char == -1:
            output_message += current_char
            count += 1
            prev_char = current_char
        else:
            if current_char == prev_char: 
                count +=1
                prev_char = current_char
            else:
                output_message+=str(count)
                output_message+=current_char 
                prev_char = current_char  
                count = 1 
    output_message += str(count)            
    return output_message
