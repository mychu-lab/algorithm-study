'''https://www.codewars.com/kata/52597aa56021e91c93000cb0'''
def move_zeros(lst):
    newlst = [ x for x in lst if x != 0]
    for y in range(0,lst.count(0)) : newlst.append(0)
    return newlst