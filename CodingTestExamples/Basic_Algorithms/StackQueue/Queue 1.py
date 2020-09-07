from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridgeQue=deque([0 for _ in range(bridge_length)])
    time=0
    i=0
    l=len(truck_weights)
    sumation=0
    while i<l:
        temp = truck_weights[i]
        sumation-=bridgeQue.pop()
        if temp+sumation<=weight:
            bridgeQue.appendleft(temp)
            sumation+=temp
            i+=1
        else:
            bridgeQue.appendleft(0)
        time+=1
    for i in range(len(bridgeQue)):
        if bridgeQue[i]!=0:
            time+=bridge_length-i
            break
    return time

# list 사용하거나 / sum(deque) 사용하거나 / truck_weights 를 deque 로 사용해도 안됨.
#
#
#