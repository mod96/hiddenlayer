from collections import deque

def solution(n, results):
    graph = {i: set() for i in range(1, n + 1)}
    for result in results:
        graph[result[0]]|={result[1]}

    for elt in graph:
        queue = deque()
        visited={elt}                           #visited 를 넣기 전에 runtime error 나옴. 꼭 넣어줘야 할듯.
        for elt_next in graph[elt]:             #답안 중에, win 과 lose 둘다 hash 로 하고 각자 한단계씩만 update 하는게 있었음. 왜?
            queue.appendleft(elt_next)
        while queue:
            it=len(queue)
            for _ in range(it):
                temp=queue.pop()
                if temp not in visited:
                    graph[elt]|=graph[temp]
                    for temp_next in graph[temp]:
                        queue.appendleft(temp_next)
                    visited|={temp}
    opponents=set(graph.keys())
    answer=0
    for player in graph:
        TF = True
        for opponent in (opponents-{player}-set(graph[player])):
            if player not in graph[opponent]:
                TF=False
                break
        if TF==True:
            answer+=1

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))