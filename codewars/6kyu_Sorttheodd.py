'''https://www.codewars.com/kata/578aa45ee9fd15ff4600090d'''
def sort_array(source_array):
    even = sorted([ n for n in source_array if n%2 != 0 ])
    return [ n if n%2 == 0 else even.pop(0) for n in source_array ]
