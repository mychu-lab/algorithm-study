'''https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004'''
def highest_rank(arr):
    max_cnt = 0
    max_value = []
    if len(arr) == 0 :
        return
    for x in set(arr) :
        cnt = arr.count(x)
        if cnt > max_cnt :
            max_value.clear()
            max_value.append(x)
            max_cnt = cnt
        elif cnt == max_cnt :
            max_value.append(x)
        else :
            pass
    return max(max_value)