def check_res(elt,res):
    target=str(elt)
    question=str(res[0])
    stri=0
    ball_stri=0
    for i in range(3):
        if target[i]==question[i]:
            stri+=1
        if question[i] in target:
            ball_stri+=1
    if res[1]==stri and res[2]==ball_stri-stri:
        return True
    else:
        return False


def solution(baseball):
    total=[int(str(i)+str(j)+str(k)) for i in range(1,10) for j in range(1,10) if j!=i for k in range(1,10) if k!=i and k!=j]
    for res in baseball:
        temp=[]
        for elt in total:
            if check_res(elt,res):
                temp.append(elt)
        total=list(temp)
    return len(total)

print(solution(	[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
print(check_res(334,[353, 1, 1]))