def solution(N, road, K):
    graph = {i: {} for i in range(1, N+1)}
    for link in road:
        a, b, c = link
        if b in graph[a]:
            graph[a][b] = min(graph[a][b],c)
        else:
            graph[a][b] = c
        if a in graph[b]:
            graph[b][a] = min(graph[b][a], c)
        else:
            graph[b][a] = c

    inf = 10**8
    dijkstra = {i:(inf,i) for i in range(1,N+1)}
    dijkstra[1] = (0,1)
    answer = 0

    while dijkstra:
        target_price, target_node = min(dijkstra.values())
        for next_node in graph[target_node]:
            if next_node in dijkstra:
                if dijkstra[next_node][0] > target_price + graph[target_node][next_node]:
                    dijkstra[next_node] = (target_price + graph[target_node][next_node], next_node)
        if target_price <= K:
            answer += 1
        del dijkstra[target_node]

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))