'''from collections import deque

def solution(jobs):
    works={}
    for job in jobs:
        works.setdefault(job[0],[]).append(job[1])

    timeline = deque(sorted(works.keys()))
    ans=0

    while timeline:
        t1=timeline.popleft()
        start=min(works[t1])
        t2=t1+start
        ans+=start

        if len(works[t1])==1:
            waiting=[]
        else:
            waiting=list(zip([start for _ in range(len(works[t1]-1))], works[t1][1:]))

        while timeline and timeline[0] <= t2:
            elt=timeline.popleft()
            waiting += list(zip([elt for _ in range(len(works[elt]))], works[elt]))

        while waiting:
            next_tup=min(waiting,key=lambda tup:tup[1])
            del waiting[waiting.index(next_tup)]
            t2+=next_tup[1]
            ans+=t2-next_tup[0]

            while timeline and timeline[0] <= t2:
                elt=timeline.popleft()
                waiting += list(zip([elt for _ in range(len(works[elt]))], works[elt]))

    return ans//len(jobs)'''
#8,18 실패

from collections import deque
import heapq
def solution(jobs):
    works={}
    for job in jobs:
        if job[0] in works:
            heapq.heappush(works[job[0]],job[1]+job[0]*10**(-4))
        else:
            works[job[0]]=[job[1]+job[0]*10**(-4)]

    timeline = deque(sorted(works.keys()))
    ans=0

    while timeline:
        t1=timeline.popleft()
        start=int(heapq.heappop(works[t1]))
        t2=t1+start
        ans+=start

        if works[t1]:
            waiting=works[t1]
        else:
            waiting=[]
        while timeline and timeline[0] <= t2:
            elt=timeline.popleft()
            for worktime in works[elt]:
                heapq.heappush(waiting,worktime)

        while waiting:
            next_tup=heapq.heappop(waiting)
            t2+=int(next_tup)
            ans+=t2-round((next_tup-int(next_tup))*10**4)

            while timeline and timeline[0] <= t2:
                elt=timeline.popleft()
                for worktime in works[elt]:
                    heapq.heappush(waiting, worktime)

    return ans//len(jobs)

#성공. tuple 의 경우 sorting 이 가능하다고 하니 그걸로 다시 가보자. 또한 heapq 도 tuple 을 지원한다고 한다.

#print(solution([[0, 3], [1, 9], [2, 6]]))
#print(solution([[0,1],[1,2],[500,6]]))
#print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]))
#print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
#print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))