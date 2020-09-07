'''from collections import deque

def solution(left, right):
    ans = 0
    left, right = deque(left), deque(right)
    while left and right:
        print(left,right)
        if left[0] > right[0]:
            ans += right.popleft()
        else:
            L, R = max(left), min(right)
            if L > right[0]:
                left.popleft()
            elif L > R:
                left.popleft()
                right.popleft()
            else:
                return ans

    return ans'''
# L > right[0] 와 L > R 조건을 저울질 해야함.
'''from collections import deque
import sys
sys.setrecursionlimit(4000)

def solution(left, right):
    ans = 0
    left, right = deque(left), deque(right)
    while left and right:
        if left[0] > right[0]:
            ans += right.popleft()
        else:
            L, R = max(left), min(right)
            left.popleft()
            if L > R:
                targ1 = solution(left,right)
                right.popleft()
                targ2 = solution(left,right)
                return ans + max(targ1, targ2)
            else:
                return ans

    return ans'''
#모든 경우의 수를 고려했으나, 너무 오래걸림 : 실패 (시간 초과)

'''def solution(left, right):
    if max(left) > max(right):
        return sum(right)
    ans = 0
    i, j, l = 0, 0, len(left)
    while i < l and j < l:
        if left[i] > right[j]:
            ans += right[j]
            j += 1
        else:
            i += 1
            if i < l:
                L, R = max(left[i:]), min(right[j:])
                if right[j] >= L:
                    j += 1
                else:
                    return ans + max(solution(left[i:],right[j:]), solution(left[i:],right[j+1:]))
            else:
                return ans
    return ans'''

'''def solution(left, right):
    ans = 0
    i, j, l, k = 0, 0, len(left), len(right)
    while i < l and j < k:
        if left[i] > right[j]:
            ans += right[j]
            j += 1
        else:
            i += 1
            if i < l:
                L, R = max(left[i:]), min(right[j:])
                if right[j] >= L:
                    j += 1
                elif L > R:
                    targ = right[j]
                    idx = int(i)
                    while left[idx] <= targ:
                        idx += 1
                    return ans + max(targ + solution(left[idx:],right[j+1:]), solution(left[i:],right[j+1:]))
                else:
                    return ans
            else:
                return ans
    return ans'''

'''def solution(left, right):
    ans = 0
    i, j, l, k = 0, 0, len(left), len(right)
    while i < l and j < k:
        targ = right[j]
        if left[i] > targ:
            ans += targ
            j += 1
        else:
            i += 1
            if i < l:
                if targ >= max(left[i:]):
                    j += 1
                else:
                    idx = int(i)
                    while left[idx] <= targ:
                        idx += 1
                    return ans + max(targ + solution(left[idx:],right[j+1:]), solution(left[i:],right[j+1:]))
            else:
                return ans
    return ans'''

'''def call(left, right):
    ans = [0]
    i, j, l, k = 0, 0, len(left), len(right)
    while i < l and j < k:
        print(left, right)
        targ = int(right[j])
        if left[i] > targ:
            ans = [a + targ for a in ans]
            j += 1
        else:
            i += 1
            if i < l:
                j += 1
                idx = int(i)
                for idx in range(i,len(left)):
                    if left[idx] > targ:
                        break
                ans += [targ + a for a in call(left[idx:], right[j:])] + call(left[i:], right[j:])
            else:
                return ans
    return ans

solution = lambda left, right : call(left, right)'''


'''def solution(left, right):
    ans = 0
    i, j, l, k = 0, 0, len(left), len(right)
    while i < l and j < k:
        targ = int(right[j])
        if left[i] > targ:
            ans += targ
            i -= 1
        elif max(left[i:]) > targ:
            i += 1
            idx = int(i)
            while left[idx] <= targ:
                idx += 1
            return ans + max(targ + solution(left[idx:],right[j+1:]), solution(left[i:],right[j+1:]))
        i += 1
        j += 1
    return ans'''
# 효율성 fail (1번만 통과 : 140ms)

'''def solution(left, right):
    ans, ate = 0, [0]
    i, j, l, k = 0, 0, len(left), len(right)
    while i < l and j < k:
        targ = int(right[j])
        if left[i] > targ:
            ans += targ
            i -= 1
        elif max(left[i:]) > targ:
            idx = int(i + 1)
            while left[idx] <= targ:
                idx += 1
            ate.append(ans + targ + solution(left[idx:],right[j+1:]))
        i += 1
        j += 1
    return max(max(ate),ans)'''
# 위에랑 시간 비슷함.

'''def solution(left, right):
    ans = 0
    i, j, l, k = 0, 0, len(left), len(right)
    while i < l and j < k:
        targ = right[j]
        if left[i] > targ:
            ans += targ
            i -= 1
            
        elif max(left[i:]) > targ:
            i += 1
            idx = int(i)
            while left[idx] <= targ:
                idx += 1
            temp=right[j+1:]
            return ans + max(targ + solution(left[idx:],temp), solution(left[i:],temp))
        i += 1
        j += 1
    return ans'''


'''def solution(left, right, i=0, j=0):
    ans = 0
    l, k = len(left), len(right)
    while i < l and j < k:
        targ = right[j]
        if left[i] > targ:
            ans += targ
            i -= 1
        elif i < l - 1:
            i += 1
            if max(left[i:]) > targ:
                idx = int(i)
                while left[idx] <= targ:
                    idx += 1
                return ans + max(targ + solution(left, right, idx, j+1), solution(left, right, i, j+1))
        i += 1
        j += 1
    return ans'''
# 효율성 1번 99 ms

'''def solution(left, right, i=0, j=0):
    ans = 0
    l, k = len(left), len(right)
    ax = left[i]
    while i < l and j < k:
        targ = right[j]
        if ax > targ:
            ans += targ
            j += 1
        elif i < l - 1:
            i += 1
            j += 1
            if max(left[i:]) > targ:
                idx = int(i)
                while left[idx] <= targ:
                    idx += 1
                return ans + max(targ + solution(left, right, idx, j), solution(left, right, i, j))
            ax = left[i]
        else:
            i += 1
            j += 1
    return ans'''
# 효율성 1번 75 ms

'''def solution(left, right, i=0, j=0):
    ans = 0
    l, k = len(left), len(right)
    ax = left[i]
    while i < l and j < k:
        targ = right[j]
        if ax > targ:
            ans += targ
            j += 1
        elif i < l - 1:
            i += 1
            possible = max(left[i:])
            all_possible = max(right[j:])
            if possible > all_possible:
                return ans + sum(right[j:])
            j += 1
            if possible > targ:
                idx = int(i)
                while left[idx] <= targ:
                    idx += 1
                return ans + max(targ + solution(left, right, idx, j), solution(left, right, i, j))
            ax = left[i]
        else:
            i += 1
            j += 1
    return ans'''
#효율성 2,3 번 fail - 1번 0.17 ms

'''def solution(left, right, i=0, j=0):
    ans = 0
    l, k, ax, l_max = len(left), len(right), left[i], max(left)
    while i < l and j < k:
        targ = right[j]
        if targ >= l_max:
            i += 1
            j += 1
            if i < l:
                ax = left[i]
        elif ax > targ:
            ans += targ
            j += 1
        elif i < l - 1:
            i += 1
            possible = max(left[i:])
            all_possible = max(right[j:])
            if possible > all_possible:
                return ans + sum(right[j:])
            j += 1
            if possible > targ:
                idx = int(i)
                while left[idx] <= targ:
                    idx += 1
                return ans + max(targ + solution(left, right, idx, j), solution(left, right, i, j))
            ax = left[i]
        else:
            return ans
    return ans'''
#효율성 2,3 번 fail - 1번 0.21 ms

'''def solution(left, right, i=0, j=0):
    ans = 0
    l, k = len(left), len(right)
    ax = left[i]
    while i < l and j < k:
        targ = right[j]
        if ax > targ:
            ans += targ
            j += 1
        elif i < l - 1:
            i += 1
            possible = max(left[i:])
            all_possible = max(right[j:])
            if possible > all_possible:
                return ans + sum(right[j:])
            j += 1
            if possible > targ:
                idx = int(i)
                while left[idx] <= targ:
                    idx += 1
                return ans + max(targ + solution(left, right, idx, j), solution(left, right, i, j))
            ax = left[i]
        else:
            i += 1
            j += 1
    return ans'''

def solution(left, right):
    l = len(left)
    table = [[0 for _ in range(l + 1)]] + [[0] + [R if R < L else 0 for R in right] for L in left]
    DP = [[0 for _ in range(l + 2) ] for _ in range(l + 2)]
    cnt = 0
    for row in range(1,l + 2):
        for col in range(1,l + 2):
            b1, b2, b3 = 0, 0, 0
            #옆에서 올 경우
            if row < l + 1 and table[row][col - 1]:
                b1 = DP[row][col - 1] + table[row][col - 1]
                if col - 1 == row + cnt:
                    cnt += 1
            #대각으로 올 경우
            if not table[row - 1][col - 1]:
                b2 = DP[row - 1][col - 1]
            #위에서 올 경우
            if col < l + 1 and not table[row - 1][col]:
                b3 = DP[row - 1][col]

            DP[row][col] = max(b1,b2,b3)

            if col > row + cnt:
                break

    return max(max(DP[-1]),max([rowlist[-1] for rowlist in DP]))
# 다른 사람이 java 로 푼 풀이에서 table 을 사용하며 for 문이 두개인 것을 보고 풀었당.


print(solution([3,2,5],[2,4,1])) # 7
print(solution([1,2,7,4,4],[2,8,8,5,3])) # 3
print(solution([7,2,7,4,4],[2,8,8,5,3])) # 10
print(solution([1,1,1,1,3],[2,3,1,1,1])) # 3
print(solution([1,1,1,1,7],[5,7,1,1,1])) # 5
print(solution([1,1,1,7,2,1,1,1,1,1,1],[5,7,1,1,1,1,1,7,1,1,1])) # 10