

def solution(N, stages):
    users = sorted(stages,reverse=True)
    i = 0
    ans = []
    for stage in range(N,0,-1):
        while i < len(users) and users[i] > stage:
            i += 1
        numer = 0
        while i < len(users) and users[i] == stage:
            i += 1
            numer += 1
        if i == 0:
            ans.append((0,-stage))
        else:
            ans.append((numer/i,-stage))

    ans.sort(reverse=True)
    answer = [-elt[1] for elt in ans]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
print(solution(5,[4,4,4]))