'''https://www.codewars.com/kata/5266876b8f4bf2da9b000362'''
def likes(names):
    who = ""
    like = "like"
    if len(names) == 0 :
        who = "no one"
        like = "likes"
    elif len(names) == 1:
        who = names[0]
        like = "likes"
    elif len(names) == 2 :
        who = names[0] + ' and ' + names[1]
    elif len(names) == 3 :
        who = names[0] + ', ' + names[1] + ' and ' + names[2]
    else :
        who = names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others'

    return who + ' ' + like + ' this'