'''https://www.codewars.com/kata/52b757663a95b11b3d00062d'''
def to_weird_case(words):
    nu = 0
    result = ""
    if len(words) == 0 :
        return result
    for w in words:
        if nu%2 == 0 :
            result = result + w.upper()
        else :
            result = result + w.lower()
        nu = nu + 1
        if w == ' ':
            nu = 0
    return result