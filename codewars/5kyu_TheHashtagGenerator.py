'''https://www.codewars.com/kata/52449b062fb80683ec000024'''
def generate_hashtag(s):
    result = '#'
    for x in s.split():
        result = result + x[0].upper() + x[1:].lower()
    if len(result) <= 1 or len(result) > 140:
        return False;
    return result