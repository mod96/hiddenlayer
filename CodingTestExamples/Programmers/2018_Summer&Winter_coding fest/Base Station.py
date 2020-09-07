def solution(n, stations, w):
    S = [elt - w - 1 for elt in stations] + [n]
    E = [1] + [elt + w + 1 for elt in stations]
    answer = 0
    for idx in range(len(S)):
        if (S[idx] - E[idx] + 1)%(2 * w + 1) == 0:
            answer += (S[idx] - E[idx] + 1) // (2 * w + 1)
        else:
            answer += (S[idx] - E[idx] + 1)//(2 * w + 1) + 1

    return answer


print(solution(11,[4,11],1))
print(solution(16,[9],2))