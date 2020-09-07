from itertools import permutations
from math import sqrt

def solution(numbers):
    max=int(sqrt(int(''.join(sorted(numbers,reverse=True)))))+1
    primes = [2]
    for i in range(3, max):
        detector=True
        for prime in primes:
            if i % prime == 0:
                detector=False
                break
        if detector:
            primes.append(i)

    def is_prime(num):
        for prime in primes:
            if (num%prime==0 or num==1) and num not in primes:
                return False
        return True

    base=[num for num in numbers]
    temp=[]
    for i in range(1,len(base)+1):
        test_set=permutations(base,i)
        for num_tuple in test_set:
            num=int(''.join(num_tuple))
            if is_prime(num) and num not in temp:
                temp.append(num)
    #print(base,temp,max)
    return len(temp)


print(solution('1235001'))