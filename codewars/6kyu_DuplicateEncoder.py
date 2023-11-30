'''https://www.codewars.com/kata/54b42f9314d9229fd6000d9c'''
def duplicate_encode(word):
    mystack = { w.lower():0 for w in word }
    for x in word:
        mystack[x.lower()] = mystack[x.lower()] + 1
    new = ""
    for y in word:
        if mystack[y.lower()] == 1:
            new = new + '('
        else :
            new = new + ')'
    return new