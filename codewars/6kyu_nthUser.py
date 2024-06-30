'''https://www.codewars.com/kata/5768b217b8ed4a77c0000c46/'''
def user_number(n):
    valid_numbers = []
    num = 1
    while len(valid_numbers) < n:
        if '4' not in str(num) and '9' not in str(num):
            valid_numbers.append(num)
        num = num+ 1
    return str(valid_numbers[n - 1])