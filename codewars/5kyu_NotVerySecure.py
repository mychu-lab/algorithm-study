'''https://www.codewars.com/kata/526dbd6c8c0eb53254000110/'''
def alphanumeric(password):
    if len(password) == 0:
        return False
    for x in password:
        if x.isdigit() == False and x.isalpha() == False:
            return False
    return True