'''https://www.codewars.com/kata/583203e6eb35d7980400002a'''
def count_smileys(arr):
    return len([ x for x in arr if (x[0] == ':' or x[0] == ';' ) and (x[-1] == ')' or x[-1] == 'D') and len(x) <=3])
arr = []
print (count_smileys(arr))
