'''https://www.codewars.com/kata/585d7d5adb20cf33cb000235'''
def find_uniq(arr):
    result = {}
    cnt = 0
    for x in arr:
        cnt = cnt + 1
        if x in result:
            result[x] = result[x] + 1
        else :
            result[x] = 1
    for key, value in result.items():
        if value == 1:
            return key