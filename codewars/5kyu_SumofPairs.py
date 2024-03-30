'''https://www.codewars.com/kata/54d81488b981293527000c8f'''
def sum_pairs(ints, s):
    nums = set()
    for x in ints:
        find = s - x
        if find in nums:
            return [find, x]
        nums.add(x)
    return None