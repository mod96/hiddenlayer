def solution(citations):
    citations.sort()
    ans = 0
    while citations:
        if citations[-1] >= ans + 1:
            citations.pop()
            ans += 1
        else:
            break

    return ans


print(solution([3,0,6,1,5]))
print(solution([6,5,5,5,3,1,0]))
print(solution([22,42]))