'''https://school.programmers.co.kr/learn/courses/30/lessons/12939'''

def solution(s):
    list = s.split(' ')
    list_i = [int(i) for i in list]
    mina = min(list_i)
    maxa = max(list_i)
    answer = str(mina) + ' ' + str(maxa)
    return answer
