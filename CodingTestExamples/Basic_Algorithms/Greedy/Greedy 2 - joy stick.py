'''def solution(name):
    dictionary={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
    answer = 0
    for elt in name:
        answer+=dictionary[elt]

    def path_finding(name,answer):
        if set(name)=={'A'}:
            return answer
        right='A'+name[1:]
        left='A'+name[::-1][:-1]

        step=1
        while right[step]=='A' and left[step]=='A' and step<len(name)//2+2 :
            step+=1
        print(step)
        answer += step
        if right[step]!='A':
            print(left,right)
            return path_finding(right,answer)
        else:
            return path_finding(left,answer)

    return path_finding(name,answer)'''

def solution(name):
    dictionary={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}
    answer = 0
    for elt in name:
        answer+=dictionary[elt]

    name_path=[1 if elt!='A' else 0 for elt in name]

    while 1 in name_path[1:]:
        right=[0]+name_path[1:]
        left=[0]+name_path[::-1][:-1]
        for i in range(1,len(name)):
            if right[i]==1:
                name_path=right[i:]+right[:i]
                break
            elif left[i]==1:
                name_path=left[i:]+left[:i]
                break
        answer+=i

    return answer




print(solution('BBABAAAB'))