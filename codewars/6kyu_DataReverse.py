'''https://www.codewars.com/kata/569d488d61b812a0f7000015'''
def data_reverse(data):
    new = []
    for i in range(int(len(data)/8)-1, -1, -1) :
        new.append(data[i*8:(i+1)*8])
    return sum(new, [])