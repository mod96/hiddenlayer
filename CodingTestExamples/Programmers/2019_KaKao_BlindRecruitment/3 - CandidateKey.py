from itertools import combinations

def solution(relation):
    columns = list(range(len(relation[0])))
    ans = []
    for col_num in range(1,1+len(columns)):
        cands = list(combinations(columns,col_num))
        for cand in cands:
            temp = []
            for row in relation:
                tup = tuple(row[col] for col in cand)
                if tup in temp:
                    break
                temp.append(tup)
            if len(set(temp)) == len(relation):
                ans.append(set(cand))
    i = 0
    while i < len(ans):
        targ = ans[i]
        j = i + 1
        while j < len(ans):
            if targ & ans[j] == targ:
                del ans[j]
            else:
                j += 1
        i += 1
    return len(ans)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
