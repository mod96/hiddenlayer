'''def solution(words):
    answer = 0
    words = [list(elt) for elt in sorted(words)]
    for idx_now in range(len(words)):
        for i in range(len(words[idx_now])):
            idx_to = idx_now + 1
            dup = False
            while idx_to < len(words) and words[idx_now][i] == words[idx_to][i]:
                dup = True
                words[idx_to][i] = '1'
                idx_to += 1
            if dup:
                words[idx_now][i] = '1'
            else:
                break
    for word in words:
        if word[-1] == '1':
            answer += len(word)
        else:
            i = 0
            while word[i] == '1':
                i += 1
            answer += i + 1

    return answer'''

def solution(words):
    answer = 0
    words = [list(elt) for elt in sorted(words)]
    for idx_now, word_now in enumerate(words):
        for i in range(len(word_now)):
            if word_now[i] != '1':
                idx_to = idx_now + 1
                dup = False
                if i == 0:
                    while idx_to < len(words) and word_now[i] == words[idx_to][i]:
                        dup = True
                        words[idx_to][i] = '1'
                        idx_to += 1
                else:
                    while idx_to < len(words) and i < len(words[idx_to]) and word_now[i] == words[idx_to][i] and words[idx_to][i-1] == '1':
                        dup = True
                        words[idx_to][i] = '1'
                        idx_to += 1
                if dup:
                    word_now[i] = '1'
                else:
                    break

    for word in words:
        if word[-1] == '1':
            answer += len(word)
        else:
            i = 0
            while word[i] == '1':
                i += 1
            answer += i + 1

    return answer

# 본인은 DP 로 풀었지만, 원래 생각했던 tree 를 정답으로 한 것이 더 깔끔함.

print(solution(['go','gone','guild'])) # 7
print(solution(['abc','def','ghi','jklm'])) # 4
print(solution(['word','war','warrior','world'])) # 15
print(solution(['aaaaa','aaaab','aaabb','aabbb','abbbb'])) # 19
print(solution(['baaaa','bbaaa','bbbaa'])) # 8