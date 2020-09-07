from collections import deque

def solution(A, B):
    A = deque(sorted(A))
    B = deque(sorted(B))
    answer = 0
    while B:
        targ = B.popleft()
        if targ > A[0]:
            A.popleft()
            answer += 1
        else:
            A.pop()
    return answer

print(solution([5,1,3,7],[2,2,6,8]))