'''https://www.codewars.com/kata/write-number-in-expanded-form-part-2'''
def expanded_form(num):
    number = str(num).split('.')
    num1 = [str(int(x) * 10 ** (len(str(number[0])) - int(index) - 1))
                for index, x in enumerate(str(number[0])) if int(x) != 0]
    num2 = [str(int(x)) + '/' + str( 10 ** (index+1))
            for index, x in enumerate(str(number[1])) if int(x) != 0]
    return ' + '.join(num1 + num2)