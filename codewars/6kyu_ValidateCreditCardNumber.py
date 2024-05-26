'''https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2'''
def validate(n):
    mod = 0
    if len(str(n))%2 == 0 :
        mod = 1
    new = [int(x) if k%2==mod else int(x)*2 for k, x in enumerate(str(n))]
    print (new)
    print (sum([ x if x< 10 else x-9 for x in new]))
    if sum([ x if x< 10 else x-9 for x in new]) % 10 == 0 :
        return True
    return False