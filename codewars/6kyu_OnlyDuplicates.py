'''https://www.codewars.com/kata/5a1dc4baffe75f270200006b'''
def only_duplicates(st):
    tmp = st
    for x in set(st) :
        if st.count(x) == 1 :
            tmp = tmp.replace(x, '')
    return tmp