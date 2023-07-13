#Consider Time Complexity
def solution(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0