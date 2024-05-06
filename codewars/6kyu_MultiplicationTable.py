'''https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08'''
def multiplication_table(size):
    result = []
    for x in range(1,size +1):
        r = []
        for y in range(1, size + 1):
            r.append(x * y)
        result.append(r)
    return result