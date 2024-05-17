'''https://www.codewars.com/kata/526989a41034285187000de4'''
def ips_between(start, end):
    cnts = {}
    for i in range(0,4):
        cnts[i] = int(end.split('.')[i]) - int(start.split('.')[i])
    cnt = 0
    for k,v in cnts.items() :
        cnt = cnt + (256 ** (3-k)) * v
    return cnt