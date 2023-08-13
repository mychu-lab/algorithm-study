'''https://school.programmers.co.kr/learn/courses/30/lessons/87390'''
def solution(n, left, right):
    answer = []
    for j in range(int(left/n), int(right/n)+1) :
        for i in range(n):
            if ((j == int(left/n)) and (i < (left%n))) or ((j == int(right/n)) and i > (right%n) ):
                continue
            answer.append(max(i+1,j+1))
    return answer
