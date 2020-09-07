'''def removal(dists):
    target = min(dists)
    target_idx = dists.index(target)
    if target_idx == 0:
        return [target + dists[1]] + dists[2:]
    elif target_idx == len(dists) - 1:
        return dists[:-2] + [target + dists[-2]]
    else:
        if dists[target_idx - 1] < dists[target_idx + 1]:
            return dists[:target_idx - 1] + [dists[target_idx - 1] + target] + dists[target_idx + 1:]
        else:
            return dists[:target_idx] + [dists[target_idx + 1] + target] + dists[target_idx + 2:]

def solution(distance, rocks, n):
    rocks.sort()
    dists = [rocks[0]] + [rocks[i+1] - rocks[i] for i in range(len(rocks)-1)] + [distance - rocks[-1]]
    for _ in range(n):
        dists = removal(dists)
    return min(dists)'''

# 위에것에서 연산속도만 빠르게 한것. 실패.
'''def removal(dists):
    target = min(dists)
    target_idx = dists.index(target)
    if target_idx == 0:
        dists[1] += target
        dists.pop(0)
    elif target_idx == len(dists) - 1:
        dists[-2] += target
        dists.pop()
    else:
        if dists[target_idx - 1] < dists[target_idx + 1]:
            dists[target_idx - 1] += target
        else:
            dists[target_idx + 1] += target
        dists.pop(target_idx)
    return dists


def solution(distance, rocks, n):
    rocks += [0,distance]
    rocks.sort()
    dists = [rocks[i+1] - rocks[i] for i in range(len(rocks)-1)]
    for _ in range(n):
        dists = removal(dists)
    return min(dists)'''
'''
def removal(dists,group):
    target = min(dists)
    target_idx = dists.index(target)
    if target_idx == 0:
        dists[1] += target
        dists.pop(0)
    elif target_idx == len(dists) - 1:
        dists[-2] += target
        dists.pop()
    else:
        if dists[target_idx - 1] < dists[target_idx + 1]:
            dists[target_idx - 1] += target
        else:
            dists[target_idx + 1] += target
        dists.pop(target_idx)
    return dists


def solution(distance, rocks, n):
    rocks += [0,distance]
    rocks.sort()
    dists = [rocks[i+1] - rocks[i] for i in range(len(rocks)-1)]
    # 인접한 것들을 n번 더할 건데 최소값이 최대가 되어야 한다.
    # 작은 애들 고르고, 두개 붙어있으면 각자 양옆이랑, 세개 이상 붙으면 밖은 밖이랑 먼저 하고 중간넘들은 작은쪽으로
    candidates = sorted(dists)[:n]
    idxs = []
    for i in range(n):
        idx = dists.index(candidates[i])
        if i > 0 and idxs[i - 1] == idx:
            idx = dists.index(candidates[i], idxs[i - 1] + 1)
            idxs.append(idx)
        else:
            idxs.append(idx)

    idxs.sort()
    groups = []
    temp = [idxs[0]]
    for i in range(1,n):
        if idxs[i - 1] + 1 == idxs[i]:
            temp.append(idxs[i])
        else:
            groups.append(temp)
            temp = [idxs[i]]
    groups.append(temp)

    for group in groups:
        if len(group) == 1:


    return 0'''

'''def idxs_to_groups(idxs):
    groups = []
    temp = [idxs[0]]
    for i in range(1, len(idxs)):
        if idxs[i - 1] + 1 == idxs[i]:
            temp.append(idxs[i])
        else:
            groups.append(temp)
            temp = [idxs[i]]
    groups.append(temp)
    return groups


def solution(distance, rocks, n):
    rocks += [0, distance]
    rocks.sort()
    dists = [rocks[i + 1] - rocks[i] for i in range(len(rocks) - 1)]

    left = min(dists)
    right = int(distance)
    while left < right:
        mid = (left + right) // 2

        idxs = [i for i in range(len(dists)) if dists[i] < mid]
        groups = idxs_to_groups(idxs)

        cnt = 0
        for group in groups:
            cnt += round(len(group)/2 + 0.1)
        print(left, right, mid, groups, cnt)
        if n < cnt:
            right = mid - 1
        elif cnt < n:
            left = mid + 1
        else:
            summed = []
            for group in groups:
                if len(group) % 2 == 0:
                    summed.append(min([dists[group[2*i]] + dists[group[2*i + 1]] for i in range(len(group)//2)]))

            if summed:
                temp = min(summed)
                if temp < mid:
                    right = mid - 1
                elif temp > mid:
                    if mid in dists:
                        return mid
                    else:
                        left = mid + 1
                elif temp == mid:
                    return mid

            for group in groups:
                if len(group) % 2 == 1:
                    cnt = 0
                    for i in range(len(group)//2):
                        if dists[group[2*i]] + dists[group[2*i+1]] < mid:
                            if dists[group[2*i]] + dists[group[2*i+1]] + dists[group[2*i+2]] < mid:
                                right = mid - 1
                            else:
                                cnt += 1
                                if cnt > 1:
                                    right = mid - 1

    return (left + right) // 2'''

'''def idxs_to_groups(idxs):
    groups = []
    temp = [idxs[0]]
    for i in range(1, len(idxs)):
        if idxs[i - 1] + 1 == idxs[i]:
            temp.append(idxs[i])
        else:
            groups.append(temp)
            temp = [idxs[i]]
    groups.append(temp)
    return groups


def solution(distance, rocks, n):
    rocks += [0, distance]
    rocks.sort()
    dists = [rocks[i + 1] - rocks[i] for i in range(len(rocks) - 1)]
    left = min(dists)
    right = int(distance)
    while left < right:
        mid = (left + right) // 2

        idxs = [i for i in range(len(dists)) if dists[i] < mid]
        if idxs:
            groups = idxs_to_groups(idxs)

            cnt = 0
            for group in groups:
                cnt += round(len(group)/2 + 0.1)
            if n < cnt:
                right = mid - 1
            elif cnt < n:
                left = mid + 1
            else:
                summed = []
                for group in groups:
                    if len(group) > 1:
                        if len(group) % 2 == 0:
                            summed.append(min([dists[group[2*i]] + dists[group[2*i + 1]] for i in range(len(group)//2)]))
                        else:
                            cnt = 0
                            i = 0
                            group.append(group[-1] + 1)
                            while i < len(group) - 2:
                                if dists[group[i]] + dists[group[i+1]] < mid:
                                    if dists[group[i]] + dists[group[i+1]] + dists[group[i+2]] < mid:
                                        right = mid - 1
                                    else:
                                        cnt += 1
                                        if cnt > 1:
                                            right = mid - 1
                                        i += 3
                                else:
                                    i += 2

                if summed:
                    temp = min(summed)
                    if temp < mid:
                        right = mid - 1
                    elif temp > mid:
                        if mid in dists:
                            return mid
                        else:
                            left = mid + 1
                    elif temp == mid:
                        return mid
        else:
            left = mid + 1

    return left'''

'''def check(mid, rocks, n):
    cnt, l, i, found = 0, len(rocks), 0, False
    while i < l - cnt - 1 and cnt <= n:
        if rocks[i+1] - rocks[i] < mid:
            rocks.pop(i+1)
            cnt += 1
        elif rocks[i+1] - rocks[i] == mid:
            found = True
            i += 1
        else:
            i += 1
    if cnt < n:
        return 'L'
    elif cnt > n:
        return 'R'
    else:
        if found:
            return 'M'
        else:
            return 'L'

def solution(distance, rocks, n):
    rocks += [0, distance]
    rocks.sort()
    left, right = 1, distance + 1
    while left < right:
        print(left,right)
        mid = (left+right) // 2
        TF = check(mid, list(rocks), n)
        if TF == 'R':
            right = mid - 1
        elif TF == 'L':
            left = mid + 1
        else:
            return mid

    if left == right:
        return left
    elif mid == left:
        return right
    else:
        return left'''

def check(mid, rocks, n):
    cnt, l, i, found = 0, len(rocks), 0, False
    while i < l - cnt - 1 and cnt <= n:
        if rocks[i+1] - rocks[i] < mid:
            if i == l - cnt - 2:
                while rocks[i+1] - rocks[i] < mid and cnt <= n:
                    rocks.pop(i)
                    cnt += 1
                    i -= 1
                break
            else:
                rocks.pop(i+1)
                cnt += 1
        else:
            i += 1
    for i in range(len(rocks)-1):
        if rocks[i+1] - rocks[i] == mid:
            found = True
            break

    if cnt < n:
        return 'L'
    elif cnt > n:
        return 'R'
    else:
        if found:
            return 'M'
        else:
            return 'L'

def solution(distance, rocks, n):
    rocks += [0, distance]
    rocks.sort()
    left, right = 1, distance + 1
    while left + 1 < right:
        mid = (left+right) // 2
        TF = check(mid, list(rocks), n)
        if TF == 'R':
            right = mid
        elif TF == 'L':
            left = mid
        else:
            return mid

    TF = check(left, rocks, n)
    if TF == 'R':
        return right
    else:
        return left

print(solution(25,[2, 14, 11, 21, 17],2))  # 4
print(solution(33,[7,12,15,21],2))  # 9
print(solution(10,[0,1,2,3,4,5,6,7,8,9,10],6))  # 1
print(solution(10,[1,2,3,4,5,6,7,8,9],5)) # 2
print(solution(34,[5,19,28],2))  # 15