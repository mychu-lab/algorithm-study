'''https://school.programmers.co.kr/learn/courses/30/lessons/12985'''
def solution(n, a, b):
    answer = 0
    while True:
        answer = answer + 1
        a = int((a+1)/2)
        b = int((b+1)/2)
        n = int(n/2)
        if a == b or n == 1:
            break;
    return answer