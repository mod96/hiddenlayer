from collections import deque

def solution(strs, t):
    l = len(t)
    graph = {l:[]}
    for idx in range(l):
        if t[idx] in strs:
            graph.setdefault(idx,[]).append(idx+1)
        if idx + 1 < l and t[idx:idx+2] in strs:
            graph.setdefault(idx,[]).append(idx+2)
        if idx + 2 < l and t[idx:idx+3] in strs:
            graph.setdefault(idx,[]).append(idx+3)
        if idx + 3 < l and t[idx:idx+4] in strs:
            graph.setdefault(idx,[]).append(idx+4)
        if idx + 4 < l and t[idx:idx+5] in strs:
            graph.setdefault(idx,[]).append(idx+5)
    BFS = None
    level = 0
    if 0 in graph:
        BFS = deque([0])
    while BFS:
        level += 1
        this_level = len(BFS)
        for _ in range(this_level):
            node = BFS.popleft()
            for next_node in graph[node]:
                if next_node == l:
                    return level
                if next_node in graph and next_node not in BFS:
                    BFS.append(next_node)
            del graph[node]
    return -1

# DP 를 이용한 풀이도 있음
# https://velog.io/@ptm0304/%EB%8B%A8%EC%96%B4%ED%8D%BC%EC%A6%90-DP-BFS
# DP[i] 를 저장할 때에는, t[i-len:i] in strs 이면 DP[i-len] + 1 을 저장해준다. len 은 5 ~ 1
# 이렇게 되면, 끝부분에 level 이 남으며 초기값(0)에서 변화가 없으면 -1 출력.

print(solution(['ab','na','n','a','bn'],'nabnabn'))
print(solution(['ba','na','n','a'],'banana'))