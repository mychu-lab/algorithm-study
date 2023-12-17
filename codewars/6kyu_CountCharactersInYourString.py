'''https://www.codewars.com/kata/52efefcbcdf57161d4000091'''
def count(s):
    return {key:s.count(key) for key in s }