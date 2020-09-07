def solution(triangle):
    L=len(triangle)
    if L==1:
        return triangle[0][0]

    for i in range(1,L):
        for j in range(i+1):
            if j==0:
                triangle[i][0]+=triangle[i-1][0]
            elif j==i:
                triangle[i][i]+=triangle[i-1][i-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])

    return max(triangle[L-1])

print(solution())