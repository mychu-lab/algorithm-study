'''https://www.codewars.com/kata/5287e858c6b5a9678200083c'''
def narcissistic( value ):
    number = str(value)
    sum = 0
    for x in number :
        sum = sum + pow(int(x), len(number))
    if sum == value :
        return True;
    return False # Code away