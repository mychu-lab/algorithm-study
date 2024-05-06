'''https://www.codewars.com/kata/53697be005f803751e0015aa'''
def encode(st):
    vowel ={'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
    newtxt = ''
    for i in st :
        if i in vowel :
            i = vowel[i]
        newtxt = newtxt + i
    return newtxt

def decode(st):
    vowel = {'1':'a', '2':'e', '3':'i', '4':'o', '5':'u'}
    newtxt = ''
    for i in st:
        if i in vowel:
            i = vowel[i]
        newtxt = newtxt + i
    return newtxt