'''https://www.codewars.com/kata/57a42ef9e298a72d710002aa'''
def how_many_step(a, b):
    tmp = b
    cnt = 0
    while tmp != a :
        cnt = cnt + 1
        if tmp%2 == 0 and tmp/2 >= a :
            tmp = tmp/2
        else :
            tmp = tmp - 1
    return cnt