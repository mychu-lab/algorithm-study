'''https://www.codewars.com/kata/54da5a58ea159efa38000836/python'''
'''python list has count() method...... '''
def find_it(seq):
    dic = {}
    for i in seq :
        if i in dic:
            dic[i] = dic[i] + 1
        else :
            dic[i] = 1

    for x in dic :
        if dic[x] % 2 == 1 :
            return x
    return 0