from collections import deque

def solution(arrangement):
    arr=deque(arrangement)
    ans=0
    stack=deque()
    while arr:
        targ=arr.popleft()
        if targ=='(':
            stack.append(targ)
            laser=True
        elif laser==True:
            stack.pop()
            ans+=len(stack)
            laser=False
        else:
            stack.pop()
            ans+=1

    return ans

print(solution('()(((()())(())()))(())'))
