'''https://www.codewars.com/kata/52bc74d4ac05d0945d00054e'''
def first_non_repeating_letter(s):
    d = { x.lower() : s.lower().count(x.lower()) for x in s }
    cnt_s = [ (i , d[i.lower()]) for i in s ]
    for x in cnt_s :
        if x[1] == 1 : return x[0]
    return ""