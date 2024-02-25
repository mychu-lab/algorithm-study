'''https://www.codewars.com/kata/517abf86da9663f1d2000003'''
def to_camel_case(text):
    result = ""
    if len(text) >0 :
        text = text.replace("_","-")
        for x in text.split("-") :
            if x.lower() == "the" or x.lower() == "a" :
                result = result + x
            else :
                result = result + x[0].upper() + x[1:]
        return  result
    return result