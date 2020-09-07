def solution(routes):
    ans = 0
    routes.sort()
    temp=[-30000,30000]
    for i in range(len(routes)):
        if routes[i][1] < temp[0] or temp[1] < routes[i][0]:
            ans+=1
            temp = routes[i]
        else:
            temp = [max(routes[i][0],temp[0]),min(routes[i][1],temp[1])]

    return ans+1

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))