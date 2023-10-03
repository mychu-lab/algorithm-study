'''https://www.codewars.com/kata/5264d2b162488dc400000001'''
def spin_words(sentence):
    new = ""
    for word in sentence.split(' ') :
        if len(word) >=5 :
            new = new + word[::-1]
        else :
            new = new + word
        new = new + ' '
    return new.rstrip()