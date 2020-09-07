import heapq

def solution(operations):
    minheap = []
    maxheap = []

    for op in operations:
        if op[0] == 'I':
            heapq.heappush(minheap, int(op[2:]))
            heapq.heappush(maxheap, -int(op[2:]))
        else:
            if minheap:
                if op[2] == '1':
                    target=-heapq.heappop(maxheap)
                    minheap.remove(target)
                    heapq.heapify(minheap)
                else:
                    target=-heapq.heappop(minheap)
                    maxheap.remove(target)
                    heapq.heapify(maxheap)

    if minheap:
        return [-maxheap[0],minheap[0]]
    else:
        return [0,0]

print(solution(['I 1', 'I 5','I 3', 'D 1']))