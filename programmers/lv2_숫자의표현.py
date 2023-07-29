'''https://school.programmers.co.kr/learn/courses/30/lessons/12924'''

def solution(n):
    answer = 1
    start = 1
    sum = 0
    while True :
        for i in range(start, n):
            sum = sum + i
            if sum == n :
                answer = answer + 1
            if sum > n :
                break;
        start= start + 1
        sum = 0
        if start == n :
            break;
        if start > int(n/2)  :
            break;
    return answer
