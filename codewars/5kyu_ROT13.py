'''https://www.codewars.com/kata/530e15517bc88ac656000716'''
def rot13(message):
    return ''.join([chr((ord(x)-97+13)%26+97) if x.isalnum() and x.islower() else chr((ord(x)-65+13)%26+65)
                    if x.isalnum() and x.isupper() else x for x in message ])