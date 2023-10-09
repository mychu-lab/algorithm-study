'''https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1'''
def duplicate_count(text):
    words={}
    cnt = 0
    for w in text :
        if str(w.lower()) in words :
            words[str(w.lower())] = words[str(w.lower())] + 1
        else :
            words[str(w.lower())] = 1

    for x in words :
        if words[x] >= 2 :
            cnt = cnt + 1
    return cnt