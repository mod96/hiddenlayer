import heapq

def solution(scov, K):
    heapq.heapify(scov)
    answer=0
    while scov[0]<K:
        first=heapq.heappop(scov)
        try:
            second=heapq.heappop(scov)
        except:
            return -1
        heapq.heappush(scov,first+2*second)
        answer+=1

    return answer