'''https://www.codewars.com/kata/55c6126177c9441a570000cc'''
def order_weight(string):
    d = []
    for x in string.split(' '):
        sum = 0
        for w in x :
            sum = sum + int(w)
        d.append((x,sum))
    return ' '.join([ k for k, v in sorted(d, key=lambda x: (x[1], str(x[0])))])