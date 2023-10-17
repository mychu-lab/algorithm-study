'''https://www.codewars.com/kata/5526fc09a1bbd946250002dc'''
def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i % 2 == 0 :
            even.append(i)
        else :
            odd.append(i)

    if len(odd) > len(even) :
        return even[0]
    else :
        return odd[0]