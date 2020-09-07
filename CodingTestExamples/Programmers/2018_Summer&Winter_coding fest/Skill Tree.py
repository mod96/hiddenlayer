def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_set, i, Possible = set(skill), 0, True
        for skill_iter in skill_tree:
            if skill_iter in skill_set and skill_iter != skill[i]:
                Possible = False
                break
            elif skill_set and skill_iter == skill[i]:
                skill_set.remove(skill[i])
                i += 1
        if Possible:
            answer += 1

    return answer

print(solution('CBD',["BACDE", "CBADF", "AECB", "BDA"]))