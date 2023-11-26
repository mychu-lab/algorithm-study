'''https://www.codewars.com/kata/576757b1df89ecf5bd00073b'''
def tower_builder(n_floors):
    mytower = []
    for x in range(0,n_floors):
        mytower.append(' '*(n_floors-x-1) + '*'*(x * 2 + 1) + ' '*(n_floors-x-1))
    return mytower
