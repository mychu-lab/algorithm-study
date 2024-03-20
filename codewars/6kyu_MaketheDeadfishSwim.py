'''https://www.codewars.com/kata/51e0007c1f9378fa810002a9'''

def parse(data):
    '''
    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array
    '''
    sum = 0
    result = []
    if len(data) == 0 :
        return []
    for x in data:
        if x == 'i' :
            sum = sum + 1
        elif x == 'd' :
            sum = sum - 1
        elif x == 's' :
            sum = sum * sum
        elif x == 'o' :
            result.append(sum)
    return result

data = "iiisdoso"
print (parse(data))

