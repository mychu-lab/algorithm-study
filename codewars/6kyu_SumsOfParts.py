'''https://www.codewars.com/kata/5ce399e0047a45001c853c2b'''
def parts_sums(ls):
    sum = 0
    result = []
    for x in reversed(ls):
        sum += x
        result.append(sum)
    result.reverse()
    result.append(0)
    return result