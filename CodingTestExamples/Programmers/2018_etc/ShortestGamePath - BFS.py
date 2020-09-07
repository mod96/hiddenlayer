'''from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    graph = {}
    for row in range(n):
        for col in range(m):
            if maps[row][col]:
                if 0 < row and maps[row-1][col]:
                    graph.setdefault((row,col),[]).append((row-1,col))
                if 0 < col and maps[row][col-1]:
                    graph.setdefault((row,col),[]).append((row,col-1))
                if row < n - 1 and maps[row+1][col]:
                    graph.setdefault((row,col),[]).append((row+1,col))
                if col < m - 1 and maps[row][col+1]:
                    graph.setdefault((row, col), []).append((row,col+1))
    BFS = deque([(0,0)])
    visited = deque()
    level = 0
    while BFS:
        level += 1
        this_level = len(BFS)
        for _ in range(this_level):
            node = BFS.popleft()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.append(next_node)
                    BFS.append(next_node)
                    if next_node == (n-1,m-1):
                        return level + 1
    return -1'''

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    graph = {}
    for row in range(n):
        for col in range(m):
            if maps[row][col]:
                if 0 < row and maps[row-1][col]:
                    graph.setdefault((row,col),[]).append((row-1,col))
                if 0 < col and maps[row][col-1]:
                    graph.setdefault((row,col),[]).append((row,col-1))
                if row < n - 1 and maps[row+1][col]:
                    graph.setdefault((row,col),[]).append((row+1,col))
                if col < m - 1 and maps[row][col+1]:
                    graph.setdefault((row, col), []).append((row,col+1))
    BFS = None
    level = 0
    if (0,0) in graph:
        BFS = deque([(0,0)])
    while BFS:
        level += 1
        this_level = len(BFS)
        for _ in range(this_level):
            node = BFS.popleft()
            for next_node in graph[node]:
                if next_node in graph and next_node not in BFS:
                    BFS.append(next_node)
                    if next_node == (n-1,m-1):
                        return level + 1
            del graph[node]
    return -1

# visited 를 사용하는 것보다 graph 에서 직접 지워주는 것이 빠름.
# 그러나 이렇게 될 경우 59번 줄에서 'next_node not in visited' 만 사용하는 것을, 중복제거를 위해 'not in BFS' 까지 해줘야 함.
# 번외로, 테케 하나가 런타임 떴었는데, (0,0) 에서 이어지는 node 가 없음에도 BFS = deque([(0,0)]) 으로 시작하면
# 바로 while 문으로 들어가기 때문에 문제가 되었음. 이를 위해 if 문을 추가함(51줄)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(solution([[1,0,1]]))