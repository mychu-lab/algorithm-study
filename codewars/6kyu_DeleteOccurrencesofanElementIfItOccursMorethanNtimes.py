'''https://www.codewars.com/kata/554ca54ffa7d91b236000023'''
def delete_nth(order,max_e):
    cnt = { x:0 for x in list(set(order))}
    result = []
    for x in order :
        if cnt[x] < max_e :
            result.append(x)
        cnt[x] = cnt[x] + 1
    return result