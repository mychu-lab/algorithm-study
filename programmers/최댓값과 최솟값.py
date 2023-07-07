def solution(s):
    list = s.split(' ')
    list_i = [int(i) for i in list]
    mina = min(list_i)
    maxa = max(list_i)
    answer = str(mina) + ' ' + str(maxa)
    return answer

print (solution("1 2 3 4"))