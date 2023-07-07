def solution(n):
    pramN = n
    answer = bin(n)
    binN = answer[2:] #2진법 전체길이
    cnt = binN.count('1') #2진법 내 1 개수

    while True  :
        pramN = pramN + 1
        if bin(pramN)[2:].count('1') == cnt:
            break

    return pramN

print ( solution(78))