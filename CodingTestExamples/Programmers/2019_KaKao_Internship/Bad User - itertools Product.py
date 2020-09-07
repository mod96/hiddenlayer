from itertools import product

def solution(user_id, banned_id):
    ban_user = {}
    for ban_idx, ban in enumerate(banned_id):
        for user_idx, user in enumerate(user_id):
            if len(ban) == len(user):
                same = True
                for i in range(len(ban)):
                    if ban[i] != '*' and ban[i] != user[i]:
                        same = False
                        break
                if same:
                    ban_user.setdefault(ban_idx,'')
                    ban_user[ban_idx] += str(user_idx)
    N = len(ban_user)
    possible = list(product(*ban_user.values()))
    possible = [tuple(sorted(elt)) for elt in possible if len(set(elt)) == N]

    return len(set(possible))

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))