'''def solution(budgets, M):
    wish=sum(budgets)
    budgets.sort()
    if wish<=M:
        return budgets[-1]
    elif budgets[0]>M/len(budgets):
        return int(M/len(budgets))
    else:
        lack=wish-M
        i=-1
        while budgets[i-1] > budgets[i] + lack/i :
            lack -= budgets[i] - budgets[i-1]
            i -= 1
        return budgets[i] + int(lack/i) - 1'''


'''def solution(budgets, M):
    budgets.sort()
    l=len(budgets)
    if sum(budgets)<=M:
        return budgets[-1]
    elif budgets[0]>M/l:
        return M//l
    else:
        i=l//2
        step=i//2
        while step != 0:
            if sum(budgets[:i])+budgets[i]*(l-i) > M:
                i-=step
                step=step//2
            else:
                i+=step
                step=step//2
        temp=sum(budgets[:i])+budgets[i]*(l-i)
        if temp> M:
            return (M-sum(budgets[:i]))//(l-i)
        elif temp ==M:
            return budgets[i]
        else:
            return (M-sum(budgets[:i+1]))//(l-i-1)'''

def solution(budgets, M):
    budgets.sort()
    l=len(budgets)
    if sum(budgets)<=M:
        return budgets[-1]
    elif budgets[0]>M/l:
        return M//l
    else:
        left=0
        right=l-1
        while left<=right:
            i=(left+right)//2
            if sum(budgets[:i])+budgets[i]*(l-i) > M:
                right=i-1
            else:
                left=i+1

        temp=sum(budgets[:i])+budgets[i]*(l-i)
        if temp> M:
            return (M-sum(budgets[:i]))//(l-i)
        elif temp ==M:
            return budgets[i]
        else:
            return (M-sum(budgets[:i+1]))//(l-i-1)

print(solution([100, 120, 100, 120, 150],400))
print(solution([1,2,3,4,5,6,7,8,9,10], 56))
print(solution([120, 110, 140, 150],485))
print(solution([100, 110, 150, 150],500))