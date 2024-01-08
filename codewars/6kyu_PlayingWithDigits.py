'''https://www.codewars.com/kata/5552101f47fc5178b1000050'''
def dig_pow(n, p):
    sum = 0
    for x in str(n) :
        sum = sum + ( int(x) ** p)
        if sum % n == 0:
            return int(sum / n )
        p = p + 1
    return -1