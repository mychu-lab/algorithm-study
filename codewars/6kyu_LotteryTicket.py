'''https://www.codewars.com/kata/57f625992f4d53c24200070e/'''
def bingo(ticket,win):
    miniwin = 0
    result = 'Loser!'
    for x in ticket:
        if chr(x[1]) in x[0] :
            miniwin += 1
    if miniwin >= win:
        result = 'Winner!'
    return result

ticket = [ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
win = 2