'''https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991'''
def rev_rot(strng, sz):
    new = ""
    if sz > 0 and strng != "" and len(strng) > sz :
        for x in range(0, len(strng)//sz ) :
            block = strng[x*sz :x*sz + sz]
            if int(sum(int(digit) for digit in block)) % 2 == 0 :
                new = new + block[::-1]
            else :
                new = new + block[1:] + block[0]
    return new