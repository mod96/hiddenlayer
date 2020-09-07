from collections import deque

def solution(n, computers):
    graph = {i: {j for j in range(n) if computers[i][j] == 1 and j != i} for i in range(n)}

    answer = 0
    while graph:
        visited = deque()
        network = deque([list(graph.keys())[0]])
        while network:
            n=network.popleft()
            if n not in visited:
                visited.append(n)
                network+=graph[n]-set(visited)
                del graph[n]
        answer+=1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))