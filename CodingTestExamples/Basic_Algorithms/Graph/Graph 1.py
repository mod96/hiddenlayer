'''from collections import deque

def solution(n, edge):
    graph={i:deque() for i in range(1,n+1)}
    for line in edge:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    dijkstra={i:(i,n) for i in range(2,n+1)}
    dijkstra.update({1:(1,0)})
    shortlengths=deque()

    while dijkstra:
        target=min(dijkstra.values(),key=lambda tup:tup[1])[0]
        for next in graph[target]:
            try:
                if dijkstra[target][1]+1<dijkstra[next][1]:
                    dijkstra[next]=(next,dijkstra[target][1]+1)
            except:
                pass
        shortlengths.append(dijkstra[target][1])
        del dijkstra[target]

    return shortlengths.count(max(shortlengths))'''


'''from collections import deque

def solution(n, edge):
    graph={i:deque() for i in range(1,n+1)}
    for line in edge:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    dijkstra={i:(i,n) for i in range(2,n+1)}
    dijkstra.update({1:(1,0)})
    answer=0
    key=0

    while dijkstra:
        target=min(dijkstra.values(),key=lambda tup:tup[1])[0]
        for next in graph[target]:
            try:
                if dijkstra[next][1]>dijkstra[target][1]+1:
                    dijkstra[next]=(next,dijkstra[target][1]+1)
            except:
                pass

        if dijkstra[target][1]==key:
            answer+=1
        elif dijkstra[target][1]>key:
            answer=1
            key=dijkstra[target][1]

        del dijkstra[target]

    return answer'''

#weight 가 없을 때에는 dijkstra 보다 bfs 를 사용하는 것이 좋다고 한다.

from collections import deque

def solution(n, edge):
    graph = {i: deque() for i in range(1, n + 1)}
    for line in edge:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    visited= {1}|{i for i in graph[1]}
    queue=deque(graph[1])

    while queue:
        it=len(queue)
        for _ in range(it):
            for node in graph[queue.pop()]:
                if node not in visited:
                    queue.appendleft(node)
                    visited|={node}

    return it



print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))