from collections import deque

def solution(s):
    stack = deque()
    for elt in s:
        if stack and stack[-1] == elt:
            stack.pop()
        else:
            stack.append(elt)

    if stack:
        return 0
    else:
        return 1

print(solution('baabaa'))