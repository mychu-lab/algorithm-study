'''https://school.programmers.co.kr/learn/courses/30/lessons/12914'''
import math
def solution(n):
    answer = 0
    k = 0
    for i in range(n, math.ceil(n/2)-1, -1):
        if n == 1 :
            answer = 1
            break;
        answer = answer + int (math.factorial(i) // (math.factorial(k) * math.factorial(i-k)))
        k = k + 1
    return answer%1234567