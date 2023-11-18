'''https://www.codewars.com/kata/5208f99aee097e6552000148'''
def solution(s):
    result = ""
    if len(s) > 0:
        for x in s :
            if x.isupper() :
                result = result + " "
            result = result + x
    return result.lstrip()