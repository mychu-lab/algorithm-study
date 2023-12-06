'''https://www.codewars.com/kata/5839edaa6754d6fec10000a2'''
def find_missing_letter(chars):
    v = ord(chars[0])
    for c in chars:
        if ord(c) - v == 2 :
            return chr(ord(c)-1)
        else :
            v = ord(c)