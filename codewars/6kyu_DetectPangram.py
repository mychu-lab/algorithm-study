'''https://www.codewars.com/kata/545cedaa9943f7fe7b000048'''
def is_pangram(s):
    result = set()
    for x in s :
        if x.isalpha():
            result.add(ord(x.lower()))
    if len(result) == 26:
        return True
    return False