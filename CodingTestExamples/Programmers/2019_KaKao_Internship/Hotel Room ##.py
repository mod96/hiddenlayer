'''import sys
sys.setrecursionlimit(2000000)
def find_room(elt,room_set,where_did):
    if elt in room_set:
        return find_room(elt+1,room_set,where_did)
    else:
        return room_set | {elt}, where_did + [elt]

def solution(k, room_number):
    room_set = set()
    where_did = []
    for elt in room_number:
        room_set, where_did = find_room(elt,room_set, where_did)

    return where_did'''
# 위의 것을 list만 가지고 해봤는데 (room_set 대신 where_did와 통합) 역시 set 사용하는게 빠르긴 함. but linear 탐색이다보니 시간초과

'''def find_room(elt,room_hash,where_did):
    if elt in room_hash:
        elt_to = room_hash[elt]
        while elt_to in room_hash:
            elt_to = room_hash[elt_to]
        next_elt = elt_to + 1
        while next_elt in room_hash:
            next_elt = room_hash[next_elt]
        room_hash[elt] = next_elt
        room_hash[elt_to] = next_elt
        return room_hash, where_did + [elt_to]
    else:
        next_elt = elt + 1
        while next_elt in room_hash:
            next_elt = room_hash[next_elt]
        room_hash[elt] = next_elt
        return room_hash, where_did + [elt]

def solution(k, room_number):
    room_hash = {}
    where_did = []
    for elt in room_number:
        room_hash, where_did = find_room(elt,room_hash, where_did)

    return where_did'''

'''def solution(k, room_number):
    room_hash = {}
    where_did = []
    for elt in room_number:
        if elt in room_hash:
            elt_to = room_hash[elt]
            while elt_to in room_hash:
                elt_to = room_hash[elt_to]
            next_elt = elt_to + 1
            while next_elt in room_hash:
                next_elt = room_hash[next_elt]
            room_hash[elt] = next_elt
            room_hash[elt_to] = next_elt
            where_did.append(elt_to)
        else:
            next_elt = elt + 1
            while next_elt in room_hash:
                next_elt = room_hash[next_elt]
            room_hash[elt] = next_elt
            where_did.append(elt)

    return where_did'''
# 효율 1,2,5,7 통과

'''def solution(k, room_number):
    room_hash = {}
    where_did = []
    for elt in room_number:
        if elt in room_hash:
            elt_to = room_hash[elt]
            while elt_to in room_hash:
                elt_to = room_hash[elt_to]
            next_elt = elt_to + 1
            temp = [elt,elt_to]
            while next_elt in room_hash:
                temp.append(next_elt)
                next_elt = room_hash[next_elt]
            for renew in temp:
                room_hash[renew] = next_elt
            where_did.append(elt_to)
        else:
            next_elt = elt + 1
            temp = [elt]
            while next_elt in room_hash:
                temp.append(next_elt)
                next_elt = room_hash[next_elt]
            for renew in temp:
                room_hash[renew] = next_elt
            where_did.append(elt)

    return where_did'''

def solution(k, room_number):
    room_hash = {}
    where_did = []
    for elt in room_number:
        print(elt,room_hash)
        if elt in room_hash:
            elt_to = room_hash[elt]
            while elt_to in room_hash:
                elt_to = room_hash[elt_to]
            next_elt = elt_to + 1
            temp = [elt,elt_to]
            while next_elt in room_hash:
                temp.append(next_elt)
                next_elt = room_hash[next_elt]
            for renew in temp:
                room_hash[renew] = next_elt
            where_did.append(elt_to)
        else:
            next_elt = elt + 1
            temp = [elt]
            while next_elt in room_hash:
                temp.append(next_elt)
                next_elt = room_hash[next_elt]
            for renew in temp:
                room_hash[renew] = next_elt
            where_did.append(elt)

    return where_did

print(solution(10,[1,3,4,1,3,1]))
print(solution(100,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))