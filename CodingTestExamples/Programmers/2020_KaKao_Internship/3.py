# BS trial

'''def solution(gems):
    group_len = len(set(gems))
    left = int(group_len)
    right = len(gems)

    while left < right:
        mid = (left + right) // 2
        check = False
        for i in range(len(gems)):
            if len(set(gems[i:i+mid])) == group_len:
                check = True
                break
        if check:
            right = mid
        else:
            left = mid + 1

    for i in range(len(gems)):
        if len(set(gems[i:i + left])) == group_len:
            return [i + 1, i + left]'''

'''def solution(gems):
    group_len = len(set(gems))
    length = int(group_len)

    while True:
        for i in range(len(gems)):
            if len(set(gems[i:i+length])) == group_len:
                return [i + 1, i + length]
        length += 1'''


# Greedy trial
'''from collections import deque

def solution(gems):
    group = set(gems)
    if len(group) == 1:
        return [1, 1]
    temp = deque([gems[0]])
    answer = []
    for i in range(1, len(gems)):
        temp.append(gems[i])
        while temp[0] in list(temp)[1:]:
            temp.popleft()
        if len(set(temp)) == len(group):
            if len(temp) == len(group):
                return [i - len(temp) + 2, i + 1]
            answer.append( (len(temp), i - len(temp) + 1, i) )
    ans = min(answer)
    return [ans[1] + 1, ans[2] + 1]'''


'''from collections import deque

def solution(gems):
    group = set(gems)
    temp = deque()
    answer = []
    for i in range(len(gems)):
        temp.append(gems[i])
        if gems[i] in group:
            group.remove(gems[i])
        while True:
            targ = temp.popleft()
            if targ not in temp:
                temp.appendleft(targ)
                break
        if not group:
            if len(temp) == len(group):
                return [i - len(temp) + 2, i + 1]
            answer.append( (len(temp), i - len(temp) + 1, i) )
    ans = min(answer)
    return [ans[1] + 1, ans[2] + 1]'''

#DP trial
'''def solution(gems):
    group_len = len(set(gems))
    DP = [0 for _ in range(len(gems) - group_len + 1)]
    for i in range(len(DP)):
        temp = set(gems[i:i + group_len])
        j = group_len
        none = None
        while len(temp) != group_len:
            if i + j == len(gems):
                none = (len(gems),len(gems),len(gems))
                break
            else:
                temp |= {gems[i + j]}
                j += 1
        if none:
            DP[i] = none
        else:
            DP[i] = (j, i + 1, i + j)
    answer = min(DP, key=lambda tup:tup[0])
    return [answer[1], answer[2]]'''

# Greedy re1
'''from collections import deque

def solution(gems):
    group_len = len(set(gems))
    temp = deque()
    k = 0
    j = 0
    while len(set(temp)) < group_len:
        temp.append(gems[j])
        j += 1
    while temp[0] in list(temp)[1:]:
        temp.popleft()
        k += 1

    answer = deque()
    answer.append( (len(temp), k, j - 1))

    for i in range(j, len(gems)):
        temp.append(gems[i])
        while temp[0] in list(temp)[1:]:
            temp.popleft()
        answer.append( (len(temp), i - len(temp) + 1, i) )

    ans = min(answer)
    return [ans[1] + 1, ans[2] + 1]'''

'''from collections import deque

def solution(gems):
    group = set(gems)
    temp = deque()
    k = 0
    j = 0
    while group:
        temp.append(gems[j])
        if gems[j] in group:
            group.remove(gems[j])
        j += 1
    while True:
        targ = temp.popleft()
        if targ not in temp:
            temp.appendleft(targ)
            break
        k += 1

    answer = deque()
    answer.append( (len(temp), k, j - 1))

    for i in range(j, len(gems)):
        temp.append(gems[i])
        while True:
            targ = temp.popleft()
            if targ not in temp:
                temp.appendleft(targ)
                break
        answer.append( (len(temp), i - len(temp) + 1, i) )

    ans = min(answer)
    return [ans[1] + 1, ans[2] + 1]'''

'''from collections import deque

def solution(gems):
    group = set(gems)
    for i in range(len(gems)):
        try:
            gems[i] = (gems[i], gems.index(gems[i],i + 1))
        except:
            gems[i] = (gems[i], len(gems))
    temp, k, j = deque(), 0, 0
    while group:
        temp.append(gems[j])
        if gems[j][0] in group:
            group.remove(gems[j][0])
        j += 1
    while temp[0][1] < j:
        temp.popleft()
        k += 1

    answer = deque()
    answer.append( (len(temp), k, j - 1))

    for i in range(j, len(gems)):
        temp.append(gems[i])
        while temp[0][1] < i + 1:
            temp.popleft()
        answer.append( (len(temp), i - len(temp) + 1, i) )

    ans = min(answer)
    return [ans[1] + 1, ans[2] + 1]'''

'''def solution(gems):
    group = set(gems)
    answer = []
    for gem in group:
        temp = [gems.index(gem)]
        while True:
            try:
                temp.append(gems.index(gem,temp[-1]+1))
            except:
                break
        if len(set(gems[0:temp[0]])) == len(group):
            answer.append((temp[0], 1, temp[0]))

        if len(set(gems[temp[-1]:])) == len(group):
            answer.append((len(gems)-temp[-1], temp[-1] + 1, len(gems)))

        for i in range(len(temp)-1):
            if len(set(gems[temp[i]:temp[i+1]])) == len(group):
                answer.append((temp[i+1] - temp[i], temp[i] + 1, temp[i+1]))

    print(answer)
    ans = min(answer)


    return [ans[1], ans[2]]'''

from collections import deque

def solution(gems):
    group = set(gems)
    l = len(gems)

    group_hash = {}
    for i in range(l):
        group_hash.setdefault(gems[i],deque()).append(i)
    for key in group_hash:
        group_hash[key].popleft()
    for i in range(l):
        try:
            gems[i] = (gems[i], group_hash[gems[i]].popleft())
        except:
            gems[i] = (gems[i], l)

    temp, k, j = deque(), 0, 0
    while group:
        temp.append(gems[j])
        if gems[j][0] in group:
            group.remove(gems[j][0])
        j += 1
    while temp[0][1] < j:
        temp.popleft()
        k += 1
    answer = deque()
    answer.append( (len(temp), k, j - 1))

    for i in range(j, l):
        temp.append(gems[i])
        while temp[0][1] < i + 1:
            temp.popleft()
        answer.append( (len(temp), i - len(temp) + 1, i) )

    ans = min(answer)
    return [ans[1] + 1, ans[2] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))  # 3,7
print(solution(["AA", "AB", "AC", "AA", "AC"]))  #1,3
print(solution(	["XYZ", "XYZ", "XYZ"]))  #1,1
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  #1,5