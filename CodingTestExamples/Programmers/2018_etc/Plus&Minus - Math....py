'''def solution(arr):
    answer = int(arr[0])
    idx = 1
    while idx < len(arr) and arr[idx] != '-':
        if idx % 2 == 0:
            answer += int(arr[idx])
        idx += 1
    idx += 1
    if idx < len(arr):
        answer -= int(arr[idx])
    idx += 1
    while idx < len(arr):
        temp = 0
        while idx < len(arr) and arr[idx] != '-':
            if idx % 2 == 0:
                temp += int(arr[idx])
            idx += 1
        idx += 1
        if idx < len(arr):
            temp -= int(arr[idx])
        idx += 1
        answer += abs(temp)

    return answer'''

def solution(arr):
    minus_index = [0]
    for cnt in range(arr.count('-')):
        minus_index.append(arr.index('-',minus_index[cnt]+1))
    minus_index.pop(0)
    answers = []
    for k in range(len(minus_index) - 1):
        minus_1 = minus_index[k]
        minus_2 = minus_index[k + 1]
        answer = int(arr[0])
        idx = 1
        while idx < minus_1:
            if arr[idx] == '+':
                answer += int(arr[idx + 1])
            else:
                answer -= int(arr[idx + 1])
            idx += 2
        while idx < minus_2:
            answer -= int(arr[idx + 1])
            idx += 2
        while idx < len(arr):
            answer += int(arr[idx + 1])
            idx += 2
        answers.append(answer)
    answer = int(arr[0])
    idx = 1
    while idx < len(arr):
        if arr[idx] == '+':
            answer += int(arr[idx + 1])
        else:
            answer -= int(arr[idx + 1])
        idx += 2
    answers.append(answer)

    return max(answers)

# 일명 '사칙연산'
# 모두 DP 로 풀었지만, 수학을 이용하면 이렇게 노가다로 풀기 가능
# 연산에는 +와 -만 있고, 가능한 계산 순서 중 최대값 찾는 문제. 숫자 최대 101개이기 때문에 완전탐색시 101!...
# - 가 두번째 나오면 그 뒤로는 모두 +로 처리 가능하기 때문에(대신 -와 - 사이에는 모두 - 처리) - index를 찾고 경우의 수 처리해줌
# 원래는 -가 2개 이상이어야만 이 전략으로 하고 아니면 주욱 순서대로 계산했는데, 테스트 1번에서 안됨.
# 1 - 2 + 100 - 3 + 1 의 경우 내 전략으로 하면 100은 + 로 처리되지 않음. 따라서 주욱 순서대로 하는 것도 answers에 넣어 처리함.


print(solution(['1','-','3','+','5','-','8']))
print(solution(['5','-','3','+','1','+','2','-','4']))
print(solution(['1','-','2','+','3','-','4','+','5','-','6','+','7','-','8']))
print(solution(['1','-','2','-','3','-','4','-','5','-','6','-','7','+','8','-','8']))
print(solution(['1','-','1','-','2','-','2','-','2']))
print(solution(['1','+','1','+','1']))
print(solution(['1','-','1','-','3','+','20','-','8']))
print(solution(['1','-','1','-','3','+','5','+','5','-','8']))