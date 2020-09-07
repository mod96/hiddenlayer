def move_to_next_coord(now,move):
    bool1 = move == 'U' and now[1] == 5
    bool2 = move == 'D' and now[1] == -5
    bool3 = move == 'L' and now[0] == -5
    bool4 = move == 'R' and now[0] == 5
    if bool1 or bool2 or bool3 or bool4:
        return now
    elif move == 'U':
        return (now[0], now[1] + 1)
    elif move == 'D':
        return (now[0], now[1] - 1)
    elif move == 'L':
        return (now[0] - 1, now[1])
    elif move == 'R':
        return (now[0] + 1, now[1])

def solution(dirs):
    moved_set = set()
    now = (0, 0)
    answer = 0
    for move in dirs:
        next_coord = move_to_next_coord(now,move)
        bool1 = (now,next_coord) in moved_set
        bool2 = now == next_coord
        if bool1 or bool2:
            pass
        else:
            moved_set |= {(now,next_coord),(next_coord,now)}
            answer += 1
        now = next_coord
    return answer


print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))