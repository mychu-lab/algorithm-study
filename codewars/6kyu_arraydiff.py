'''https://www.codewars.com/kata/523f5d21c841566fde000009/python'''
def array_diff(a, b):
    result = []
    for x in b :
        cnt = 0
        for y in a :
            if x == y :
                a[cnt] = ''
            cnt = cnt + 1

    for do in a:
        if do != '' :
            result.append(do)
    return result
