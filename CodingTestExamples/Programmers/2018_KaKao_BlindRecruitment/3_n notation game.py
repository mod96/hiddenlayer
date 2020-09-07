'''from collections import deque

def solution(n, t, m, p):
    full = [str(i) for i in range(10)] + ['A','B','C','D','E','F']
    num_set = [full[i] for i in range(n)]

    num_iter = deque(num_set[1:])
    num_line = '0'
    while len(num_line) <= t * m + p:
        l = len(num_iter)
        for i in range(l):
            targ = num_iter.popleft()
            num_iter.append('0' + targ)
            if targ[0] != '0':
                num_line += targ
            for j in range(1,n):
                num_iter.append(num_set[j] + targ)
    print(num_line)
    answer = ''
    for i in range(t):
        answer += num_line[i * m + p - 1]
    return answer'''

'''from collections import deque

def solution(n, t, m, p):
    full = [str(i) for i in range(10)] + ['A','B','C','D','E','F']
    num_set = [full[i] for i in range(n)]

    num_iter = deque(num_set)
    num_line = ''.join(num_set)
    while len(num_line) <= t * m + p:
        l = len(num_iter)
        for elt in list(num_iter):
            num_iter.append('0'+elt)
        for i in range(l):
            targ = num_iter.popleft()
            for j in range(1,n):
                num_iter.append(num_set[j] + targ)
                num_line += num_set[j] + targ
    answer = ''
    for i in range(t):
        answer += num_line[i * m + p - 1]
    return answer'''

def solution(n, t, m, p):
    full = [str(i) for i in range(10)] + ['A','B','C','D','E','F']
    num_set = [full[i] for i in range(n)]

    def num_to_Str(num, n):
        if num < n:
            return num_set[num]
        else:
            return num_to_Str(num // n, n) + num_set[num % n]

    num_line = ''
    num = 0
    while len(num_line) <= (t-1) * m + p:
        num_line += num_to_Str(num,n)
        num += 1

    answer = ''
    for i in range(t):
        answer += num_line[i * m + p - 1]
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))