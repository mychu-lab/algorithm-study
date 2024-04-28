'''https://www.codewars.com/kata/59c633e7dcc4053512000073'''
def solve(s):
    sum = 0
    result = []
    cnt = 0
    for x in s :
        cnt = cnt + 1
        if x in 'aeiou':
            result.append(sum)
            sum = 0
        else :
            sum = sum + (ord(x) - 96)
        if cnt == len(s):
            result.append(sum)
    return max(result)