from collections import deque

def solution(priorities, location):
    key=priorities[location]
    priorities[location]=key-0.5
    answer=0
    for i in range(9,key,-1):
        if i in priorities:
            l=len(priorities)
            i_count=priorities.count(i)
            answer+=i_count
            i_last=l-list(reversed(priorities)).index(i)
            for j in range(i_last):
                if priorities[j]!=i:
                    priorities.append(priorities[j])
            priorities=priorities[i_last:]
    temp=priorities.index(key-0.5)
    for i in range(temp):
        if priorities[i]==key:
            answer+=1

    return answer+1

#print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))