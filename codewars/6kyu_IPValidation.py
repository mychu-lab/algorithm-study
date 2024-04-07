'''https://www.codewars.com/kata/515decfd9dcfc23bb6000006'''
def is_valid_IP(strng):
    if strng.count('.') == 3 :
        cnt = 0
        for x in strng.split('.') :
            if len(x) == 0 :
                return False
            if x[0] == '0' and len(x) > 1:
                return False
            if x.isdigit() and int(x) >=0 and int(x) <= 255 :
                cnt += 1
        if cnt == 4 :
            return True
    return False