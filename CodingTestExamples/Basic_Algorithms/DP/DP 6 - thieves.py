'''def solution(money):
    l, ans = len(money), []
    for start, idx in [(money[0],0), (money[1],1)]:
        level, std = [(start,idx)], l - 1 + idx
        while len(level) < l//2 + 1:
            next_level = [0 for _ in range(len(level)+1)]
            # only for 0
            if level[0] and level[0][1] + 2 < std:
                next_level[0] = (level[0][0] + money[level[0][1] + 2],level[0][1] + 2)
            elif level[0]:
                ans.append(level[0][0])
            # only for -1
            if level[-1] and level[-1][1] + 3 < std:
                next_level[-1] = (level[-1][0] + money[level[-1][1] + 3],level[-1][1] + 3)
            elif level[-1]:
                ans.append(level[-1][0])
            # for general occasions
            for i in range(1,len(level)):
                b1, b2 = -1, -1
                if level[i-1] and level[i-1][1] + 3 < std:
                    b1 = level[i-1][0] + money[level[i-1][1] + 3]
                elif level[i-1]:
                    ans.append(level[i-1][0])
                if level[i] and level[i][1] + 2 < std:
                    b2 = level[i][0] + money[level[i][1] + 2]
                elif level[i]:
                    ans.append(level[i][0])
                if b1 > -1 or b2 > -1:
                    if b1 > b2:
                        next_level[i] = (b1, level[i-1][1] + 3)
                    else:
                        next_level[i] = (b2, level[i][1] + 2)
            level = list(next_level)

    return max(ans)'''


#나한테 오는 것이 2개나 3개 전에서 왔다.
'''def solution(money):
    l = len(money)

    # idx 0 선택
    temp1 = list(money)
    temp1[2] += temp1[0]
    if l > 3:
        temp1[3] += temp1[0]
    if l > 4:
        temp1[4] += temp1[2]
    if l > 5:
        for i in range(5,l):
            temp1[i] += max(temp1[i-2],temp1[i-3])
    ans = max(temp1[-2],temp1[-3])

    #idx 1 선택
    if l > 3:
        money[3] += money[1]
    if l > 4:
        money[4] += money[1]
    if l > 5:
        money[5] += money[3]
    if l > 6:
        for i in range(6,l):
            money[i] += max(money[i-2],money[i-3])
    ans = max(ans, money[-1], money[-2])

    return ans'''
# 위의 경우, 1번집이나 2번집을 기준으로 시작했다. 하지만 3번 기준으로 시작해야 할 때도 있다.

def solution(money):
    l = len(money)

    # idx 0 선택
    temp = list(money)
    temp[1] = temp[0]
    temp[2] += temp[0]
    if l > 3:
        for i in range(3,l):
            temp[i] += max(temp[i-2],temp[i-3])
    ans = max(temp[-2],temp[-3])

    #idx 0 선택 안함 (1, 2 시작 가능)
    money[0] = 0
    money[2] = max(money[1],money[2])
    if l > 3:
        for i in range(3,l):
            money[i] += max(money[i-2],money[i-3])
    ans = max(ans, money[-1], money[-2])

    return ans



print(solution([1,2,3,1])) # 4
print(solution([7,6,3,4,5,6,2,1])) # 17