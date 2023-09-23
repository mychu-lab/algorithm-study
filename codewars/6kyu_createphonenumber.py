'''https://www.codewars.com/kata/525f50e3b73515a6db000b83'''
def create_phone_number(n):
    result = '('
    region = n[:3]
    num1 = n[3:6]
    num2 = n[6:]
    for x in region :
        result = result + str(x)
    result = result + ') '
    for y in num1 :
        result = result + str(y)
    result = result + '-'
    for z in num2 :
        result = result + str(z)
    return result
