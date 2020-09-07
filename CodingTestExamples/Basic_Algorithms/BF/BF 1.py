def solution(answers):
    l=len(answers)
    M=[0,0,0]
    M[0]=[1+i%5 for i in range(l)]
    m2={1:1,3:3,5:4,7:5}
    M[1]=[2 if i%2==0 else m2[i%8] for i in range(l)]
    m3={0:3,1:3,2:1,3:1,4:2,5:2,6:4,7:4,8:5,9:5}
    M[2]=[m3[i%10] for i in range(l)]
    corr = [sum([1 if answers[i] == M[j][i] else 0 for i in range(l)]) for j in range(3)]
    answer=[]
    for i in range(3):
        if corr[i]==max(corr):
            answer.append(i+1)
    return answer

answers=[1,2,3,4,5]
print(solution(answers))