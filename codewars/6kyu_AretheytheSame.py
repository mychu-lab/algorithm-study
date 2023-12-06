'''https://www.codewars.com/kata/550498447451fbbd7600041c'''
def comp(array1, array2):
    if array1 is not None and array2 is not None:
        return sorted([n**2 for n in array1]) == sorted(array2)
    return False