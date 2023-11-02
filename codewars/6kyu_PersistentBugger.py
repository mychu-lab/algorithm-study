'''https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec'''
def persistence(n):
    cnt = 0
    while n >= 10 :
        result = 1
        for x in str(n):
            result = result * int(x)
        n = result
        cnt = cnt + 1
    return cnt