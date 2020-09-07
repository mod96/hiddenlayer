'''def solution(n, times):
    t=0
    while n>1:
        for officer in times:
            if not t % officer:
                n -= 1
                if n == 1:
                    t-=1
                    break
        t += 1

    return t'''

'''def solution(n, times):
    l=len(times)
    key=min(times)
    left=key*(n//l) if n%l==0 else key*(n//l+1)
    right=max(times)*(n//l+1)
    while left <= right:
        mid=(left+right)//2
        temp=sum(list(map(lambda x: mid//x,times)))
        if temp<n:
            left=mid+1
        elif temp==n:
            while temp==n:
                mid-=1
                temp = sum(list(map(lambda x: mid // x, times)))
            return mid+1
        else:
            if sum(list(map(lambda x: (mid-1) // x, times)))<n:
                return mid
            else:
                right=mid-1'''

def solution(n, times):
    l=len(times)
    dilig=min(times)
    left=dilig*(n//l) if n%l==0 else dilig*(n//l+1)
    right=max(times)*(n//l+1)
    while left <= right:
        mid=(left+right)//2
        key=sum(list(map(lambda x: mid//x,times)))
        if key<n:
            left=mid+1
        elif key==n: #여기서 처음에 linear search 썼는데, 이렇게 바꾸니 거의 1/10 수준으로 줄었음.
            modulus=list(map(lambda x: mid%x,times))
            return mid-min(modulus)
        else:
            if sum(list(map(lambda x: (mid-1) // x, times)))<n:
                return mid
            else:
                right=mid-1




#print(left, right,mid,temp,list(map(lambda x: mid//x,times)))

from random import randint

for _ in range(10):
    print(solution(randint(1,50),[randint(1,30) for _ in range(10)]))