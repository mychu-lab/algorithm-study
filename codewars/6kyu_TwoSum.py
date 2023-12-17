'''https://www.codewars.com/kata/52c31f8e6605bcc646000082'''
def two_sum(numbers, target):
    indx = 0
    for x in numbers:
        indy = 0
        for y in numbers :
            if indy != indx and (x + y) == target:
                if (x + y) == target:
                    return (indx, indy)
            indy = indy + 1
        indx = indx + 1