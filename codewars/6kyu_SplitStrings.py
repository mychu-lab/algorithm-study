'''https://www.codewars.com/kata/515de9ae9dcfc28eb6000001'''
def solution(s):
    result = []
    word = ''
    if len(s) > 0 :
        for x in s :
            word = word + x
            if len(word) == 2 :
                result.append(word)
                word = ''
    if len(s) % 2 == 1 :
        result.append(s[-1]+'_')
    return result