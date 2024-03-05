'''https://www.codewars.com/kata/55c04b4cc56a697bb0000048'''
def scramble(s1, s2):
    #dn = {i: s1.count(i) for i in s1} -- O(n^2)
    if len(s1) == 0 :
        return False
    if len(s2) == 0 :
        return True
    dn = {}
    for char in s1:
        if char in dn:
            dn[char] += 1
        else:
            dn[char] = 1
    cnt = 0
    for x in s2 :
        if x not in dn:
            return False
        if dn[x] == 0 :
            return False
        if x in dn:
            dn[x] = dn[x] - 1
            cnt = cnt + 1
        if cnt == len(s2) :
            return True