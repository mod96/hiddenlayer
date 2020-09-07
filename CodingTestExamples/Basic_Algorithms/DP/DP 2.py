def solution(N):
    tiles=[1,1]
    if N==1:
        return 4
    for i in range(1,N+1):
        tiles.append(tiles[-1]+tiles[-2])
    return 2*(2*tiles[N-1]+tiles[N-2])

print(solution(2))