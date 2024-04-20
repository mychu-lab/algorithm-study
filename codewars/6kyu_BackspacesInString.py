'''https://www.codewars.com/kata/5727bb0fe81185ae62000ae3'''
def clean_string(s):
    new = ""
    for w in s :
        if w == '#':
            l = len(new)
            if l >= 1 :
                new = new[:l-1]
            else :
                new = ""
        else :
            new = new + w
    return new