'''https://www.codewars.com/kata/593a061b942a27ac940000a7'''
def getting_mad(arr):
    if len(arr) != len(set(arr)):
        return 0
    i=0
    minabs = []
    while i < len(arr) - 1 :
        minabs.append(abs(sorted(arr)[i]-sorted(arr)[i+1] ))
        i = i + 1
    return min(minabs)