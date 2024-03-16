'''https://www.codewars.com/kata/54a91a4883a7de5d7800009c'''
def increment_string(string):
    if len(string) > 0 :
        num = ''
        n = len(string)
        for x in reversed(string) :
            if x.isdigit() :
                num = x + num
            else :
                break;
            n = n - 1
    else :
        return "1"
    if num == '' :
        return string + '1'
    mid = len(string) - n - len(str(int(num) + 1))
    return string[0:n] + string[n:n+mid]+ str(int(num) + 1)
