'''https://www.codewars.com/kata/546f922b54af40e1e90001da'''
def alphabet_position(text):
    new=''
    for x in text:
        if ord(x.lower()) > 96 :
            new = new + ' ' + str(ord(x.lower())-96)
    return new.lstrip()