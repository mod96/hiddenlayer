from collections import deque

def solution(weight):
    weight = deque(sorted(weight))
    if weight[0] != 1:
        return 1
    else:
        available = weight.popleft()
        while weight and available + 1 >= weight[0]:
            available += weight.popleft()
        return available + 1

print(solution([3, 1, 6, 2, 7, 30, 1]))
print(solution([1,1,1,1,1,1,1,1]))