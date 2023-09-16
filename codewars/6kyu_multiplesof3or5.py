'''https://www.codewars.com/kata/514b92a657cdc65150000006/python'''
def solution(number):
    answer = 0
    if number <= 0 :
        return 0
    for x in range(1,number):
        if x%3 == 0 or x%5 == 0 :
            answer = answer + x
    return answer