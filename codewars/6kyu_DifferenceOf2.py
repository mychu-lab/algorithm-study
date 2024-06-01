'''https://www.codewars.com/kata/5340298112fa30e786000688'''
def twos_difference(lst):
    result = []
    print (sorted(lst))
    i = 0
    while i < len(lst) -1:
        if sorted(lst)[i + 1] - sorted(lst)[i] == 2:
            result.append((sorted(lst)[i], sorted(lst)[i + 1]))
        if i < len(lst) - 2 :
            if sorted(lst)[i+1] - sorted(lst)[i] == 1 \
                    and sorted(lst)[i+2] - sorted(lst)[i] == 2 :
                result.append((sorted(lst)[i], sorted(lst)[i+2]))
        i = i + 1
    return result