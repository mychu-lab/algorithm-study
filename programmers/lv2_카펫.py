'''https://school.programmers.co.kr/learn/courses/30/lessons/42842'''

def solution(brown, yellow):
    answer = []
    whsum = int (brown / 2) + 2
    whmultiple = yellow + 2 * whsum - 4

    for i in range(1, whmultiple):
        x = i
        y = whmultiple / i
        if x + y == whsum :
            answer.append(int(y))
            answer.append(x)
            break;

    return answer