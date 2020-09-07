from collections import deque

def solution(land, height):
    N = len(land)
    group = list(land)
    for row in range(N):
        for col in range(N):
            targ = land[row][col]
            if abs(targ - land[row][col]):
                group


    answer = 0
    return answer