import string
from collections import deque

def solution(msg):
    dictionary = dict(zip(string.ascii_uppercase, [i for i in range(1,27)]))
    msg = deque(msg)
    answer = []
    idx = 27
    while msg:
        w = msg.popleft()
        while msg and w + msg[0] in dictionary:
            w += msg.popleft()
        answer.append(dictionary[w])
        if msg:
            dictionary[w + msg[0]] = idx
            idx += 1

    return answer


print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))