def solution(N, number):
    dp=[[] for _ in range(8)]
    dp[0]=[N]
    for i in range(1,8):
        if int(str(N)*(i+1))==number:
            return i+1
        else:
            dp[i]=[int(str(N)*(i+1))]

        for j in range(0,i//2+1):
            for prv in set(dp[j]):
                for prv2 in set(dp[i-j-1]):
                    if prv!=0 and prv2!=0:
                        new=[prv+prv2,prv-prv2,prv*prv2,int(prv/prv2),prv2-prv,int(prv2/prv)]
                        if number in new:
                            return i+1
                        else:
                            dp[i]+=new
    return -1


