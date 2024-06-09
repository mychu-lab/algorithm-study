'''https://www.codewars.com/kata/59175441e76dc9f9bc00000f'''
def atomic_number(electrons):
    remain_electrons = electrons
    n = 1
    nums = []
    while n > 0 :
        print (remain_electrons)
        if remain_electrons <= 2 * n * n :
            nums.append(remain_electrons)
            return nums;
        else :
            nums.append(2 * n * n)
            remain_electrons = remain_electrons - 2 * n * n
            n = n + 1