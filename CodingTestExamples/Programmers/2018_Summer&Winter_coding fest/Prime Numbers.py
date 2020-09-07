from itertools import combinations

def solution(nums):
    primes = []
    upper = 3 * max(nums) + 1
    for i in range(3,upper,2):
        is_prime = True
        sqrt = int(i ** (0.5)) + 1
        for j in range(3,sqrt):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    answer = 0
    possibles = list(combinations(nums,3))
    for tup in possibles:
        targ = sum(tup)
        if targ in primes:
            answer += 1

    return answer

print(solution([1,2,4,6,7]))