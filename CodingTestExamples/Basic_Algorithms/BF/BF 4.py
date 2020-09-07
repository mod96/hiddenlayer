from math import sqrt

def solution(brown, yellow):
    total = brown+yellow
    candidates = []
    for i in range(3,int(sqrt(total))+2):
        if total%i == 0:
            candidates.append( (total//i,i) )

    for can in candidates:
        if 2*(can[0]+can[1])-4 == brown:
            return [can[0], can[1]]

print(solution(10,2))
