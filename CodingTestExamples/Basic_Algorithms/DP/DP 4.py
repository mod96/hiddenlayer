def solution(m, n, puddles):
    DP = [[0 for i in range(n+1)] for j in range(m+1)]
    DP[1][1] = 1
    for puddle in puddles:
        DP[puddle[0]][puddle[1]] = None
    for i in range(1,n+1):
        for j in range(1,m+1):
            a , b = DP[j][i-1] , DP[j-1][i]
            if (i == 1 and j == 1) or (a == None and b == None) or DP[j][i] == None:
                pass
            elif a == None:
                DP[j][i] = b
            elif b == None:
                DP[j][i] = a
            else:
                DP[j][i] = a + b

    return DP[m][n]%1000000007
#문제를 잘 읽자. 1000000007 때문에 뻘짓 많이했다.

'''def solution(m, n, puddles):
    DP = [[0 for i in range(n+1)] for j in range(m+1)]
    DP[0][1] = 1
    for puddle in puddles:
        DP[puddle[0]][puddle[1]] = None
    for i in range(1,n+1):
        for j in range(1,m+1):
            a, b = DP[j][i-1], DP[j-1][i]
            if a != None and b != None and DP[j][i] != None:
                DP[j][i] = a + b
            elif (a == None and b == None) or DP[j][i] == None:
                pass
            elif a == None:
                DP[j][i] = b
            elif b == None:
                DP[j][i] = a
    return DP[m][n]%1000000007''' # if문 순서 바꿔줘서 3배가량 빨라졌으나 위에 것이 더 깔끔해서 위에것으로 제출함.

print(solution(4,3,[[2, 2]]))
print(solution(4,3,[[1,3],[3,1]]))