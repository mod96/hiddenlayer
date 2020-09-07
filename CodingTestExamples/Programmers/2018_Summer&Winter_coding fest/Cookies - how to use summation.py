'''from itertools import combinations

def solution(cookie):
    answer = 0
    bulkhead = list(combinations([i for i in range(len(cookie)+1)],3))
    for i, j, k in bulkhead:
        temp = sum(cookie[i:j])
        if temp > answer and temp == sum(cookie[j:k]):
            answer = temp

    return answer'''


'''import sys
sys.setrecursionlimit(10000)
def solution(cookie):

    def calc(left,mid,right,UD):
        if left == mid or mid == right:
            return 0
        L, R = sum(cookie[left:mid]), sum(cookie[mid:right])
        if L == R:
            print([cookie[left:mid],cookie[mid:right]])
            return L
        elif L < R:
            temp1 = calc(left,mid,right-1,0)
            temp2 = 0
            if UD != 'D':
                temp2 = calc(left,mid+1,right,'U')
            return max(temp1,temp2)
        else:
            temp1 = calc(left+1,mid,right,0)
            temp2 = 0
            if UD != 'U':
                temp2 = calc(left,mid-1,right,'D')
            return max(temp1,temp2)

    left, mid, right = 0, len(cookie)//2, len(cookie)

    return calc(left,mid,right,0)'''

# 구간합을 많이 사용할 경우 미리 구해놓으면 O(N) 으로 사용 가능하다.
# 모든 경우를 보는 것은 맞으나, 계산 중 discard 가능해야 하므로 combination 을 사용하지 않는다.

def solution(cookie):
    cookie_sum = [0, cookie[0]]  # sum([cookie[i:j]) = cookie_sum[j] - cookie_sum[i]
    for i in range(1,len(cookie)):
        cookie_sum.append(cookie_sum[-1] + cookie[i])

    Sum = lambda i,j : cookie_sum[j] - cookie_sum[i]
    answer = 0
    answer_max = cookie_sum[-1] // 2
    N = len(cookie)

    # left : 0 ~ N-2 , mid : left+1 ~ N-1 , right : mid+1 ~ N
    for left in range(0,N-1):
        for mid in range(left+1,N):
            targ1 = Sum(left,mid)
            if targ1 <= answer:
                continue
            elif targ1 > Sum(mid,N):
                break
            else:
                for right in range(mid+1,N+1):
                    targ2 = Sum(mid,right)
                    if targ1 < targ2:
                        break
                    elif targ1 == targ2:   # know that targ1 > answer
                        answer = targ1
                        if targ2 == answer_max:
                            return targ1
    return answer

# 답안 맨 위에 accumulate (start ~ end 의 합을 빠르게 구해주는 itertools 내장함수) 사용한 것이 있음
# mid 하나 정해서 양방향으로 accumulate 하는 방식인데 이건 왜 시간초과가 안될까..?


print(solution([1,1,2,3]))  # 3
print(solution([8,1,1,1,1,1,1,1,1]))  # 8
print(solution([1,2,3,4,5,6,7,8,9]))  # 15