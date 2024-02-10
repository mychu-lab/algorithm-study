'''https://www.codewars.com/kata/556deca17c58da83c00002db'''
def tribonacci(signature, n):
    tribs = []
    for i in range(0,n):
        if i == 0 or i == 1 or i == 2:
            tribs.append(signature[i])
            continue
        tribs.append(tribs[i-3] + tribs[i-2]+ tribs[i-1])
    return tribs