'''def solution(n, costs):
    graph={i:{} for i in range(n)}
    for line in costs:
        graph[line[0]][line[1]]=line[2]
        graph[line[1]][line[0]]=line[2]
    BF=[]
    for node in graph:
        cost=0
        visited=[node]
        while len(visited) < n:
            next_candidates = sorted(graph[node],key = lambda h:graph[node][h])
            for next in next_candidates:
                if next not in visited:
                    visited.append(next)
                    cost += graph[node][next]
                    node = next
                    break
        BF.append(cost)
    return min(BF)'''

'''import heapq
from copy import deepcopy as dcp

def solution(n, costs):
    graph={i:[] for i in range(n)}
    for line in costs:
        heapq.heappush(graph[line[0]], line[2] + line[1] * 10 ** (-2))   #{ node : cost.XX where XX=next node }
        heapq.heappush(graph[line[1]], line[2] + line[0] * 10 ** (-2))
    BF=[float('inf')]
    for node in graph:
        graph_copy=dcp(graph)
        cost=0
        visited=[node]
        while len(visited) < n and cost < BF[0]:
            next = heapq.heappop(graph_copy[node])
            while round((next - int(next)) * 10 ** 2) in visited:
                next = heapq.heappop(graph_copy[node])
            cost += int(next)
            node = round((next - int(next)) * 10 ** 2)
            visited.append(node)
        if len(visited) == n:
            heapq.heappush(BF, cost)
    return BF[0]'''

#kruskal algorithm 이 적용되는 조건이 이 문제 자체이다. 최소 비용으로, 무향그래프를, 잇기만 하는 것.
#kruskal algorithm + union find 를 위한 트리를 사용했다. 다만 업데이트를 위해 이중트리를 사용한 것이 특징이다.
#이를 MST 라고 한다. (minimum spanning tree)
#MST 를 해결하는 알고리즘은 kruskal, prim algorithm 이 있다.

def solution(n, costs):
    find_parent = {i:i for i in range(n)}
    find_children = {i:[i] for i in range(n)}
    lines = 0
    costs.sort(key = lambda multi : multi[2])
    ans = 0
    for i in range(len(costs)):
        node1, node2, cost = costs[i][0], costs[i][1], costs[i][2]
        if find_parent[node1] == find_parent[node2]:
            pass
        else:
            for children in find_children[find_parent[node2]]:
                find_parent[children] = find_parent[node1]
                find_children[find_parent[node1]].append(children)
            ans += cost
            lines += 1
            if lines == n-1:
                break
    return ans

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))