def solution(lines):
    for idx,line in enumerate(lines):
        temp = line.split()
        [hour, minute, sec] = temp[1].split(':')
        time = int(hour) * 60 * 60 * 1000 + int(minute) * 60 * 1000 + int(sec[:2]) * 1000 + int(sec[3:])
        temp2 = temp[2][:-1].split('.')
        if len(temp2) == 1:
            interval = int(temp2[0]) * 1000
        else:
            interval = int(temp2[0]) * 1000 + int(temp2[1])
        lines[idx] = (time - interval + 1, time)

    answer = 0
    for line in lines:
        for elt in line:
            for time_point in [elt, elt + 999]:
                cnt = 0
                for line in lines:
                    if time_point - 999 <= line[1] <= time_point:
                        cnt += 1
                    elif time_point - 999 <= line[0] <= time_point:
                        cnt += 1
                    elif line[0] <= time_point - 999  and time_point <= line[1]:
                        cnt += 1

                if cnt > answer:
                    answer = int(cnt)
    return answer

print(solution([
    '2016-09-15 01:00:04.001 2.0s',
    '2016-09-15 01:00:07.000 2s'
    ]))

print(solution([
    '2016-09-15 01:00:04.002 2.0s',
    '2016-09-15 01:00:07.000 2s'
    ]))
inp = [
    '2016-09-15 20:59:57.421 0.351s',
    '2016-09-15 20:59:58.233 1.181s',
    '2016-09-15 20:59:58.299 0.8s',
    '2016-09-15 20:59:58.688 1.041s',
    '2016-09-15 20:59:59.591 1.412s',
    '2016-09-15 21:00:00.464 1.466s',
    '2016-09-15 21:00:00.741 1.581s',
    '2016-09-15 21:00:00.748 2.31s',
    '2016-09-15 21:00:00.966 0.381s',
    '2016-09-15 21:00:02.066 2.62s'
    ]
print(solution(inp))