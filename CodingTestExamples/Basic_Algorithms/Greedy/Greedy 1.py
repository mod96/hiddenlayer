def solution(n, lost, reserve):
    i=0
    while i < len(lost):
        if lost[i] in reserve:
            idx = reserve.index(lost[i])
            del reserve[idx]
            del lost[i]
            i -= 1
        i+=1
    i=0
    while i<len(lost):
        if lost[i]-1 in reserve:
            idx=reserve.index(lost[i]-1)
            del reserve[idx]
            del lost[i]
            i-=1
        elif lost[i]+1 in reserve:
            idx = reserve.index(lost[i]+1)
            del reserve[idx]
            del lost[i]
            i -= 1
        i+=1

    return n-len(lost)