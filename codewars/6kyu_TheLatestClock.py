'''https://www.codewars.com/kata/58925dcb71f43f30cd00005f'''
from itertools import permutations
def latest_clock(a, b, c, d):
    makesense = [ (x[0]*10 + x[1])*60 + x[2]*10 + x[3] for x in list(permutations([a,b,c,d], 4))
                    if (x[0]*10 + x[1]) < 24 and (x[2]*10 + x[3]) < 60]
    return str('{0:02d}'.format(max(makesense)//60))+':'+str('{0:02d}'.format(max(makesense)%60))