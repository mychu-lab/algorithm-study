'''https://www.codewars.com/kata/5848565e273af816fb000449'''
def encrypt_this(text):
    result = ""
    if len(text) > 0 :
        for word in text.split(' '):
            if len(word) == 1:
                result = result + str(ord(word[0])) + ' '
            elif len(word) == 2:
                result = result + str(ord(word[0])) + word[1] + ' '
            else :
                result = result + str(ord(word[0])) + word[-1] + word[2:len(word) - 1] + word[1] + ' '
    return result.rstrip()