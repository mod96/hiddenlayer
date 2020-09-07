def solution(stones, k):
    right = 2 * 10 ** 8
    left = 0
    while left <= right:
        mid = (left + right) // 2
        temp = 0
        for stone in stones:
            if stone <= mid:
                temp += 1
            else:
                temp = 0
            if temp == k:
                right = mid - 1
                break
        if temp < k:
            left = mid + 1


    return left

print(solution([2,4,5,3,2,1,4,2,5,1],3)) # 3
print(solution([5,5,5,5,5,5,5],2)) # 5
print(solution([6,4,4,4,6,6,6,6],2)) # 4