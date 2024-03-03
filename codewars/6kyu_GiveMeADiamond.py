'''https://www.codewars.com/kata/5503013e34137eeeaa001648'''
def diamond(n):
    if n <= 0 or n%2 == 0 :
        return None
    result = ""
    for i in range(0,n):
        result = result + (' ' * abs(int( n/2 ) - i) + '*' * (n - abs(int( n/2 ) - i ) *2) + '\n')
    return result