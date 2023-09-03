'''https://school.programmers.co.kr/learn/courses/30/lessons/12945'''
def solution(n):
    a = 0
    b = 1
    if n == 0 :
        answer = 0
    if n == 1 :
        answer = 1
    if n > 1 :
        for x in range(1, n) :
            c = a%1234567 + b%1234567
            answer = c
            a = b
            b = c
    return answer%1234567