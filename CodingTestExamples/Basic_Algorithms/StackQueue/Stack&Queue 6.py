from collections import deque

def solution(pr, sp):
    l=len(pr)
    date=deque([(100-pr[i])//sp[i] if (100-pr[i])%sp[i]==0 else (100-pr[i])//sp[i]+1 for i in range(l)])
    answer = []
    while date:
        go=date.popleft()
        temp=1
        try:
            while date[0]<=go:
                date.popleft()
                temp+=1
        except:
            pass
        answer.append(temp)

    return answer


print(solution([93,30,55],[1,30,5]))