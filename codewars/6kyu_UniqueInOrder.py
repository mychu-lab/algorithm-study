'''https://www.codewars.com/kata/54e6533c92449cc251001667'''
def unique_in_order(sequence):
    uq = 0
    if len(sequence) == 0 :
        return [];
    new = [sequence[0]]
    for x in sequence:
        if x != new[-1] :
            new.append(x)
    return new