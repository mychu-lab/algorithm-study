'''https://www.codewars.com/kata/5592e3bd57b64d00f3000047'''
def find_nb(m):
    i = 1
    sum = 0
    while sum < m :
        sum = sum + i ** 3
        if sum == m :
            return i
        i = i + 1
    return -1