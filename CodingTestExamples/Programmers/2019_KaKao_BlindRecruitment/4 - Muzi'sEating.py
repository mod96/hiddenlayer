import sys
sys.setrecursionlimit(10 ** 8)

def reducing(food_times_and_idxs,k):
    K = int(k)
    next_food_times_and_idxs = []
    if food_times_and_idxs:
        skip_rotation = K // len(food_times_and_idxs)
        if skip_rotation:
            for food in food_times_and_idxs:
                if food[1] <= skip_rotation:
                    K -= food[1]
                else:
                    K -= skip_rotation
                    next_food_times_and_idxs.append((food[0],food[1]-skip_rotation))
            return reducing(next_food_times_and_idxs, K)
        else:
            return food_times_and_idxs, K
    else:
        return food_times_and_idxs, K

def solution(food_times, k):
    food_times_and_idxs = [[i,elt] for i, elt in enumerate(food_times)]
    food_times_and_idxs, k = reducing(food_times_and_idxs, k)
    if food_times_and_idxs:
        return food_times_and_idxs[k][0] + 1
    else:
        return -1

print(solution([3,1,2],5)) # 1
print(solution([5,4,3,2,1],100))