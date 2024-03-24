'''https://www.codewars.com/kata/52f787eb172a8b4ae1000a34'''
def zeros(n):
    cnt5 = 0
    i = 5
    while n // i >= 1 :
        cnt5 = cnt5 + n // i
        i = i * 5
    return cnt5
