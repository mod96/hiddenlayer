def solution(genres, plays):
    best1={}
    best2={}
    for i in range(len(genres)):
        best1.setdefault(genres[i],[]).append(plays[i])
        best2.setdefault(genres[i],[]).append((i,plays[i]))

    gen=list(best1.keys())
    gen.sort(key=lambda key : sum(best1[key]),reverse=True)

    answer = []
    for elt in gen:
        temp=best2[elt]
        temp.sort(key=lambda tup : tup[1],reverse=True)
        for i in range(len(temp)):
            if i<2:
                answer.append(temp[i][0])

    return answer

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]))