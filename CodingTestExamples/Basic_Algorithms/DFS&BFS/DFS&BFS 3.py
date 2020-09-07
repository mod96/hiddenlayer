from collections import deque

def connection(begin, target, l):
    count = 0
    for i in range(l):
        if begin[i] != target[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    l = len(begin)
    graph = {begin : {word for word in words if connection(begin, word, l)}}
    for word in words:
        graph[word] = {next_word for next_word in words if connection(word, next_word, l)}
    level = deque([begin])
    visited = deque()
    cnt = 0
    while level:
        visited += level
        L = len(level)
        for _ in range(L):
            node = level.popleft()
            if node == target:
                return cnt
            level += graph[node] - set(visited)
        cnt += 1

    return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))