'''https://school.programmers.co.kr/learn/courses/30/lessons/12981'''
def solution(n, words):
    answer = [0,0]
    result = {k: [] for k in range(0, n)}
    seek = []
    for i in range(0,len(words)):
        index = (i % n)
        result[index].append(words[i])
        if i > 0 and (seek.count(words[i]) == 1 or words[i][0] != seek[-1][-1]):  #이미 말한거 있거나, 틀렸으면 끝이다
            answer[0] = index + 1
            answer[1] = len(result[index])
            break
        seek.append(words[i])
    return answer
