# 연습문제 '도둑잡기' 랑 똑같음 (길이 1,2 조건만 추가하면 되는듯)
def solution(money):
    l = len(money)
    # 예외처리
    if l == 1:
        return money[0]
    if l == 2:
        return max(money)

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