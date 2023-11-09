'''https://www.codewars.com/kata/55c45be3b2079eccff00010f'''
def order(sentence):
    dict = {}
    txt = ""
    if len(sentence) > 0 :
      words = sentence.split(' ')
      for w in words :
          for x in w :
              if x.isdigit() :
                  dict[x] = w
                  break;

    for i in range(1,len(dict)+1):
        txt = txt + dict[str(i)] + " "
    return txt.rstrip()