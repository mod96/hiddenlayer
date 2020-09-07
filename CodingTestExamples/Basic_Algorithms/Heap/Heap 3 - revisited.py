from collections import deque
import heapq
#tuple 은 앞에꺼부터 정렬한다고 함. jobs 에서 바로바로 pop 할것이기에 jobs 는 (걸리는 시간, 요청시각) 으로 정렬한다.
def solution(jobs):
    l=len(jobs)
    jobs=deque(sorted( [(job[1],job[0]) for job in jobs],key=lambda tup:(tup[1],tup[0]) ))
    ans=0
    while jobs:
        empty_in=jobs.popleft()
        t1=empty_in[1]
        t2=t1+empty_in[0]
        ans+=empty_in[0]
        waiting=[]
        while jobs and jobs[0][1]<=t2:
            heapq.heappush(waiting,jobs.popleft())
        while waiting:
            next_tup=heapq.heappop(waiting)
            t2+=next_tup[0]
            ans+=t2-next_tup[1]
            while jobs and jobs[0][1] <= t2:
                heapq.heappush(waiting, jobs.popleft())

    return ans//l



print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))