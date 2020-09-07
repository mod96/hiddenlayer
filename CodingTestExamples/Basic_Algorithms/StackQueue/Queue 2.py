def solution(heights):
    signals=[]
    l=len(heights)
    answer = [0]*l

    for i in range(l-1,-1,-1):
        target=heights[i]
        j=0
        while j<len(signals):
            if target>signals[j][0]:
                answer[signals[j][1]]=i+1
                del signals[j]
                j-=1
            j+=1

        signals.append( (target,i) )

    return answer

heights=[6,9,5,7,4]
solution(heights)