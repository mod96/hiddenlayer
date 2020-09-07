def solution(prices):
    l=len(prices)
    ans=[0 for _ in range(l)]

    for i in range(l-1):
        for j in range(i+1,l):
            if prices[i]>prices[j]:
                break
        ans[i]=j-i

    return ans

print(solution([1, 2, 3, 2, 3]))