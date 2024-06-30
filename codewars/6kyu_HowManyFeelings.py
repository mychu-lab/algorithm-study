'''https://www.codewars.com/kata/5a33ec23ee1aaebecf000130'''
def count_feelings(st, arr):
    cnt = 0
    for words in arr :
        isfeel = True;
        for x in words :
            if len(words) > len(st):
                isfeel = False;
            if x not in st :
                isfeel = False;
        if isfeel :
            cnt = cnt + 1
    if cnt == 1 :
        txt = ' feeling.'
    else :
        txt = ' feelings.'
    return str(cnt) + txt