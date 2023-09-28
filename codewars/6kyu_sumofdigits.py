'''https://www.codewars.com/kata/541c8630095125aba6000c00'''
def digital_root(n):
    target = n
    while True :
        sum = 0
        number = str(target)
        for x in number:
            sum = sum + int(x)
        if sum < 10 :
            break;
        target = sum
    return sum