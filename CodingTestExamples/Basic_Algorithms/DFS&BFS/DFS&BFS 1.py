from collections import deque

def solution(numbers, target):
    summed=deque([numbers[0],-numbers[0]])
    for i in range(1,len(numbers)):
        iteration=len(summed)
        for j in range(iteration):
            bfr=summed.pop()
            summed.appendleft(bfr-numbers[i])
            summed.appendleft(bfr+numbers[i])

    return summed.count(target)

print(solution([1, 1, 1, 1, 1],3))

#원래 생각했던, (+x,-x),(+y,-y),... 만드는 것은 itertools 의 product 를 사용하면 된다고 한다.