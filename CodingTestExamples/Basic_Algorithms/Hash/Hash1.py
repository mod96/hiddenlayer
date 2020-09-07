participant=['leo', 'kiki', 'eden']
completion=['eden', 'kiki']


def solution(participant, completion):
    A=sorted(participant)
    B=sorted(completion)
    for i in range(len(B)):
        if A[i]!=B[i]:
            return A[i]
    return A[-1]

print(solution(participant, completion))