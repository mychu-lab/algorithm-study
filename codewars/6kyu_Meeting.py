'''https://www.codewars.com/kata/59df2f8f08c6cec835000012'''
def meeting(s):
    new = []
    for name in s.split(';') :
        new.append((name.upper().split(':')[1], name.upper().split(':')[0]))
    return ''.join(map(str,sorted(new, key=lambda x: (x[0],x[1])))).replace('\'','')