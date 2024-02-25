'''https://www.codewars.com/kata/587731fda577b3d1b0001196'''
def camel_case(s):
    result = ""
    if len(s) > 0 :
        words = s.rstrip().lstrip().split(" ")
        for x in words:
            result = result + x[0].upper() + x[1:]
    return result