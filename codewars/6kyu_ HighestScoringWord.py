'''https://www.codewars.com/kata/57eb8fcdf670e99d9b000272'''
def high(x):
    topword = ""
    topscore = 0
    for w in x.split(" "):
        curr_score = 0
        for i in w:
            curr_score = curr_score + (ord(i) - 96)
        if curr_score > topscore :
            topword = w
            topscore = curr_score
    return topword