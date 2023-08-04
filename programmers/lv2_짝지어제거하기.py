'''https://school.programmers.co.kr/learn/courses/30/lessons/12973'''

def solution(s):
    answer = 0
    stack = []
    for i in s :
        if len(stack) == 0 :
            stack.append(i)
        else :
            if i != stack[-1] :
                stack.append(i)
            elif i == stack[-1] :
                stack.pop()

    if len(stack) == 0 :
        answer = 1
    return answer