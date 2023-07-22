def solution(s):
    answer = ''
    words= s.split(' ')
    new_words = []
    for w in words :
        ind = 0
        temp_word = ''
        for i in w :
            if ind == 0 : 
                temp_word = temp_word + i.upper()
            else :
                temp_word = temp_word + i.lower()
            ind = ind + 1 
        new_words.append(temp_word)

    len_n = len(new_words)
    print (len_n)
    ii = 0 
    for x in new_words :
        if ii == 0 :
            answer = answer + x 
        else :
            answer = answer + ' ' + x
        ii = ii + 1 

    return answer
