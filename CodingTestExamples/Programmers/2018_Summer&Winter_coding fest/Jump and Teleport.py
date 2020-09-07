def solution(n):
    answer = 0
    while n != 1:
        if n % 2 != 0:
            answer += 1
        n //= 2
    return answer + 1