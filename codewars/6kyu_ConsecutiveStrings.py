'''https://www.codewars.com/kata/56a5d994ac971f1ac500003e'''
def longest_consec(strarr, k):
    if len(strarr) == 0 or k <= 0 or k > len(strarr) :
        return ""
    else:
        lens = [len(x) for x in strarr]
        summ = 0
        ind = 0
        for i in range(0,len(lens)-k+1):
            if sum(lens[i:i+k]) > summ :
                summ = sum(lens[i:i+k])
                ind = i
        return  ''.join(strarr[ind:ind+k])