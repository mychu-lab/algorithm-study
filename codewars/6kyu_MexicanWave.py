'''https://www.codewars.com/kata/58f5c63f1e26ecda7e000029'''
def wave(people):
    words = []
    for ind, w in enumerate(people.lower()) :
        if w == ' ':
            continue
        else :
            words.append(people.lower()[:ind]+people.lower()[ind].upper()+people.lower()[ind+1:])
    return words