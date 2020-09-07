stock=20
dates=[4,10,15,16,17,20]
supplies=[20,5,10,15,30,50]
k=100

'''def solution(stock, dates, supplies, k):
    dates.reverse()
    supplies.reverse()
    answer=0
    now=0
    def choosing(answer,now,stock,dates,supplies,k):
        if now+stock>k:
            return answer
        i=len(dates)-1
        temp={}
        while i>=0 and now<dates[i]<=now+stock:
            temp[supplies.pop()]=dates.pop()
            i-=1
        now+=stock
        stock=max(temp)
        answer+=1
        return choosing(answer,now,stock,dates,supplies,k)

    return choosing(answer, now, stock, dates, supplies, k)

solution(stock, dates, supplies, k)'''


def solution(stock, dates, supplies, k):
    answer=0
    i=0
    l=len(dates)
    while stock<k:
        while i<l and dates[i]<=stock:
            i+=1
        idx=supplies.index(max(supplies[0:i]))
        stock+=supplies[idx]
        supplies[idx]=0
        answer+=1

    return answer

print(solution(stock, dates, supplies, k))