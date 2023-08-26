'''https://school.programmers.co.kr/learn/courses/30/lessons/12949'''
def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for x in range(len(arr1[0])):
                answer[i][j] = answer[i][j] + arr1[i][x] * arr2[x][j]
    return answer