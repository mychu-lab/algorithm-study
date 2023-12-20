'''https://www.codewars.com/kata/5842df8ccbd22792a4000245'''
def expanded_form(num):
    nums = [ str(int(x)*10**(len(str(num))-int(index)-1)) for index, x in enumerate(str(num)) if int(x) != 0 ]
    return ' + '.join(nums)