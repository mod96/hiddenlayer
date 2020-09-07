'''from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    ans = 0
    while people:
        ans += 1
        boat = [people.popleft()]
        if people and people[0] <= limit-sum(boat):
            i=1
            while people[i] <= limit-sum(boat):
                i+=1
            boat.append(people[i-1])
            del people[i-1]

    return ans'''
#효율성 1,2,3

'''from collections import deque

def solution(people, limit):
    people_hash = {elt : people.count(elt) for elt in set(people)}
    people_key = deque(sorted(people_hash.keys()))
    ans = 0
    while people_key:
        ans += 1
        first = people_key[0]
        if people_hash[first] == 1:
            people_key.popleft()
        else:
            people_hash[first] -= 1

        i = 0
        try:
            while people_key[i] <= limit-first:
                i += 1
        except:
            pass
        finally:
            i -= 1
            if i > -1:
                second=people_key[i]
                if people_hash[second] == 1:
                    people_key.remove(second)
                else:
                    people_hash[second] -= 1

    return ans'''
#효율성 1,3

from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    ans = 0
    while people:
        if limit-people[0] < people[-1]:
            people.pop()
            ans+=1
        if limit-people[-1] < people[0]:
            people.pop()
            ans+=1
        l=len(people)
        if l == 1:
            ans+=1
            break
        elif l == 0:
            break
        if limit-people[0] >= people[-1]:
            people.pop()
            people.popleft()
            ans+=1

    return ans


print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))
