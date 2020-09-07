'''def solution(tickets):
    cnt = 0
    l=len(tickets)
    for i in range(l):
        for j in range(l):
            if i != j:
                if tickets[i] == tickets[j]:
                    cnt += 1
    while cnt:
        pass
    answer = []
    return answer''' # 확인결과 중복티켓 존재함.

'''from collections import deque
from copy import deepcopy as dc

def solution(tickets):
    l = len(tickets)
    graph = {}
    for ticket in tickets:
        graph.setdefault(ticket[0],[]).append(ticket[1])
        if ticket[1] not in graph:
            graph[ticket[1]] = []

    for key in graph:
        graph[key] = deque(sorted(graph[key], reverse = True))

    num_to_visit = {}
    for key in graph:
        for elt in graph[key]:
            num_to_visit.setdefault(elt,0)
            num_to_visit[elt] += 1
    num_to_visit.setdefault('ICN', 0)
    num_to_visit['ICN'] += 1
    print(num_to_visit)

    DFS_path = deque()
    stack = deque(['ICN'])


    while len(DFS_path) < l+1:
        node = stack.pop()
        if node == 'recall':
            recall = DFS_path.pop()
            num_to_visit[recall] += 1
            node = stack.pop()
        print(node)
        if graph[node] and num_to_visit[node] != 0:
            DFS_path.append(node)
            num_to_visit[node] -= 1
            stack += deque(['recall']) + graph[node]
        elif len(DFS_path) == l and num_to_visit[node] != 0:
            DFS_path.append(node)

    return list(DFS_path)'''

from collections import deque

def solution(tickets):
    tickets.sort(reverse = True)
    l = len(tickets)
    graph = {}
    start = []
    for i in range(l):
        if tickets[i][0] == 'ICN':
            start.append(i)
        for j in range(l):
            if i != j:
                if tickets[i][1] == tickets[j][0]:
                    graph.setdefault(i,deque()).append(j)
        if i not in graph:
            graph[i] = deque()

    DFS = deque()

    for start_node in reversed(start):
        stack = deque([start_node])
        while stack and len(DFS) < l:
            node = stack.pop()
            if node == 'L':
                DFS.pop()
            elif node not in DFS:
                DFS.append(node)
                stack += deque(['L']) + graph[node]

        if len(DFS) == l:
            ans = [tickets[i][0] for i in DFS] + [tickets[DFS[-1]][1]]
            return ans



print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))