'''https://www.codewars.com/kata/52f78966747862fc9a0009ae'''
def calc(expr):
    nums = []
    sum = 0
    operations = ['+','-','*','/']
    if len(expr) == 0:
        return sum;
    for x in expr.split(' '):
        if x in operations:
            b = nums.pop()
            a = nums.pop()
            if x == '+' :
                sum = a + b
            elif x == '-' :
                sum = a - b
            elif x == '*' :
                sum = a * b
            elif x == '/' :
                sum = a / b
            nums.append(sum)
        else :
            if x.isnumeric() :
                nums.append(int(x))
            else :
                nums.append(float(x))
    return nums.pop()