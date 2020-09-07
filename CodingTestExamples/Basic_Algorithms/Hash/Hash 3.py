def solution(clothes):
    selection={}
    for cloth in clothes:
        selection.setdefault(cloth[1],1)
        selection[cloth[1]] += 1

    answer=1
    for num in selection.values():
        answer*=num

    return answer-1

