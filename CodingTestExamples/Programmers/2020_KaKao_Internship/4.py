'''def min_path(left,up,right,down):
    inf = 10**10
    if left[1] == 2:
        left_price = (inf,2)
    elif left[1] == 1:
        left_price = (left[0] + 600, 0)
    else:
        left_price = (left[0] + 100, 0)

    if up[1] == 2:
        up_price = (inf,2)
    elif up[1] == 0:
        up_price = (up[0] + 600, 1)
    else:
        up_price = (up[0] + 100, 1)

    if right[1] == 2:
        right_price = (inf,2)
    elif right[1] == 1:
        right_price = (right[0] + 600, 0)
    else:
        right_price = (right[0] + 100, 0)

    if down[1] == 2:
        down_price = (inf,2)
    elif down[1] == 0:
        down_price = (down[0] + 600, 1)
    else:
        down_price = (down[0] + 100, 1)

    check = sorted([left_price,up_price,right_price,down_price])
    if check[0][0] == check[1][0] and check[0][1] != check[1][1] and check[0][1] != 2 and check[1][1] != 2:
        return (check[0][0], -1)

    if check[0][0] == check[2][0] and check[0][1] != check[2][1] and check[0][1] != 2 and check[2][1] != 2:
        return (check[0][0], -1)

    return check[0]


def solution(board):
    l = len(board)
    DP = [[(0,2) for i in range(l+2)] for j in range(l+2)]  # (price, from) - from : 쌉가능 -1 가로 0 세로 1 불가능 2
    for i in range(l+2):
        DP[i][0] = (0,2)
        DP[0][i] = (0,2)
        DP[i][-1] = (0,2)
        DP[-1][i] = (0,2)

    DP[1][1] = (0,-1)

    for _ in range(5):
        for row in range(1,l+1):
            for col in range(1,l+1):
                if (row, col) != (1, 1) and board[row-1][col-1] == 0:
                    DP[row][col] = min_path(DP[row][col-1],DP[row-1][col],DP[row][col+1],DP[row+1][col])


    return DP[-2][-2][0]'''

'''def hori_price(hori):
    inf = 10**10
    if hori[1] == 2:
        return (inf,2)
    elif hori[1] == 1:
        return (hori[0] + 600, 0)
    else:
        return (hori[0] + 100, 0)

def vert_price(vert):
    inf = 10**10
    if vert[1] == 2:
        return (inf,2)
    elif vert[1] == 0:
        return (vert[0] + 600, 1)
    else:
        return (vert[0] + 100, 1)

def solution(board):
    l = len(board)
    DP = [[[(0,2)] for i in range(l+2)] for j in range(l+2)]  # (price, from) - from : 쌉가능 -1 가로 0 세로 1 불가능 2
    DP[1][1] = [(0,-1)]

    for _ in range(625):
        for row in range(1,l+1):
            for col in range(1,l+1):
                if (row, col) != (1, 1) and board[row-1][col-1] == 0:
                    leftright_prices = sorted([hori_price(elt) for elt in DP[row][col-1] + DP[row][col+1]])
                    leftright_min = leftright_prices[0]
                    updown_prices = sorted([vert_price(elt) for elt in DP[row-1][col] + DP[row+1][col]])
                    updown_min = updown_prices[0]

                    if leftright_min[0] == updown_min[0] and leftright_min[1] != 2 and updown_min[1] != 2:
                        DP[row][col] = [(leftright_min[0],-1)]
                    else:
                        DP[row][col] = [leftright_min, updown_min, leftright_prices[1], updown_prices[1]]
        #print(DP)

    return DP[-2][-2][0][0]'''

'''def solution(board):
    l = len(board)
    links = {}
    for row in range(l):
        for col in range(l):
            if board[row][col] == 0:
                if row > 0 and board[row-1][col] == 0:
                    links.setdefault((row,col),[]).append((row-1,col))
                if col > 0 and board[row][col-1] == 0:
                    links.setdefault((row,col),[]).append((row,col-1))
                if row < l - 1 and board[row+1][col] == 0:
                    links.setdefault((row,col),[]).append((row+1,col))
                if col < l - 1 and board[row][col+1] == 0:
                    links.setdefault((row,col),[]).append((row,col+1))
    inf = 10 ** 10
    dijkstra = {node : (inf,2,node) for node in links}          # (price, from) - from : 쌉가능 -1 가로 0 세로 1 불가능 2
    dijkstra[(0,0)] = (0,-1,(0,0))
    key = (l-1,l-1)
    visited = []
    answer=[]
    while dijkstra:
        node = min(dijkstra.values())[2]
        visited.append(node)
        for next_node in links[node]:
            if next_node not in visited:
                if dijkstra[node][1] == 2:
                    pass
                elif dijkstra[node][1] == 1:   #node 는 세로로 오는중
                    if node[1] - next_node[1] == 0:   #node와 next_node 는 column이 같음 ( 세로로 차이남 )
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 1,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 0:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)
                    else:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 600:
                            dijkstra[next_node] = (dijkstra[node][0] + 600, 0,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 600:
                            if dijkstra[next_node][1] == 1:
                                dijkstra[next_node] = (dijkstra[node][0] + 600, -1, next_node)
                elif dijkstra[node][1] == 0:   #node 는 가로로 오는중
                    if node[0] - next_node[0] == 0:   #node와 next_node 는 row가 같음 ( 가로로 차이남 )
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 0,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 1:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)
                    else:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 600:
                            dijkstra[next_node] = (dijkstra[node][0] + 600, 1,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 600:
                            if dijkstra[next_node][1] == 0:
                                dijkstra[next_node] = (dijkstra[node][0] + 600, -1, next_node)
                else:
                    if node[0] - next_node[0] == 0:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 0,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 1:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)
                    else:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 1,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 0:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)

                if next_node == key:
                    answer.append(dijkstra[key])
        del dijkstra[node]

    return min(answer)[0]'''

def solution(board):
    l = len(board)
    links = {}
    for row in range(l):
        for col in range(l):
            if board[row][col] == 0:
                if row > 0 and board[row-1][col] == 0:
                    links.setdefault((row,col),[]).append((row-1,col))
                if col > 0 and board[row][col-1] == 0:
                    links.setdefault((row,col),[]).append((row,col-1))
                if row < l - 1 and board[row+1][col] == 0:
                    links.setdefault((row,col),[]).append((row+1,col))
                if col < l - 1 and board[row][col+1] == 0:
                    links.setdefault((row,col),[]).append((row,col+1))
    inf = 10 ** 10
    dijkstra = {node : [(inf,2,node)] for node in links}          # (price, from) - from : 쌉가능 -1 가로 0 세로 1 불가능 2
    dijkstra[(0,0)] = [(0,-1,(0,0))]
    key = (l-1,l-1)
    visited = []
    answer=[]
    while dijkstra:
        temp = []
        for elt in dijkstra:
            temp += dijkstra[elt]
        node = min(temp)[2]
        visited.append(node)
        for next_node in links[node]:
            if next_node not in visited:
                if dijkstra[node][1] == 2:
                    pass
                elif dijkstra[node][1] == 1:   # node 는 세로로 오는중
                    if node[1] - next_node[1] == 0:   # node와 next_node 는 column이 같음 ( 세로로 차이남 )
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 1,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 0:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)
                    else:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 600:
                            dijkstra[next_node] = (dijkstra[node][0] + 600, 0,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 600:
                            if dijkstra[next_node][1] == 1:
                                dijkstra[next_node] = (dijkstra[node][0] + 600, -1, next_node)
                elif dijkstra[node][1] == 0:   # node 는 가로로 오는중
                    if node[0] - next_node[0] == 0:   # node와 next_node 는 row가 같음 ( 가로로 차이남 )
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 0,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 1:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)
                    else:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 600:
                            dijkstra[next_node] = (dijkstra[node][0] + 600, 1,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 600:
                            if dijkstra[next_node][1] == 0:
                                dijkstra[next_node] = (dijkstra[node][0] + 600, -1, next_node)
                else:
                    if node[0] - next_node[0] == 0:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 0,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 1:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)
                    else:
                        if dijkstra[next_node][0] > dijkstra[node][0] + 100:
                            dijkstra[next_node] = (dijkstra[node][0] + 100, 1,next_node)
                        elif dijkstra[next_node][0] == dijkstra[node][0] + 100:
                            if dijkstra[next_node][1] == 0:
                                dijkstra[next_node] = (dijkstra[node][0] + 100, -1, next_node)

                if next_node == key:
                    answer.append(dijkstra[key])
        del dijkstra[node]

    return min(answer)[0]

#900
print(solution([[0,0,0],[0,0,0],[0,0,0]]))
#3800
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
#2100
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
#3200
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
#3000
print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1],[0,1,1,0,0]]))