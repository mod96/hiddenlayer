def solution(records):
    uid_to_name = {}
    for record in records:
        temp = record.split()
        if len(temp) == 3:
            _, uid, name = record.split()
            uid_to_name[uid] = name


    answer = []
    for record in records:
        temp = record.split()
        if len(temp) == 3:
            ent, uid, _ = temp
        else:
            ent, uid = temp
        if ent[0] == 'E':
            answer.append(uid_to_name[uid] + "님이 들어왔습니다.")
        elif ent[0] == 'L':
            answer.append(uid_to_name[uid] + "님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))