def solution(n,a,b):
    a, b= sorted([a,b])
    level, m = 0, int(n)
    while m != 1:
        m //= 2
        level += 1
    left, right= 0, n
    while True:
        mid = (left + right) // 2
        if a <= mid < b:
            return level
        elif mid <= a:
            left = mid
        else:
            right = mid
        level -= 1

print(solution(8,4,7))
print(solution(8,3,7))