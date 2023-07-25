'''https://school.programmers.co.kr/learn/courses/30/lessons/12941'''

def solution(A, B):
    answer = 0
    A_sorted = sorted(A)
    B_sorted = sorted(B, reverse=True)

    for i in range(0,len(A)):
        answer = answer + A_sorted[i] * B_sorted[i]

    return answer
