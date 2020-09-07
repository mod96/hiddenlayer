
def distance(where,to):
    x = abs(where[0] - to[0])
    y = abs(where[1] - to[1])
    return x + y

def solution(numbers, hand):
    answer = ''
    left, right = (0,0), (0,0)
    location = {1:(0,3),4:(0,2),7:(0,1),3:(0,3),6:(0,2),9:(0,1),2:(1,3),5:(1,2),8:(1,1),0:(1,0)}
    for num in numbers:
        if num in {1,4,7}:
            answer += 'L'
        elif num in {3,6,9}:
            answer += 'R'
        else:
            L = distance(left,location[num])
            R = distance(right,location[num])
            if L > R:
                answer += 'R'
            elif R > L:
                answer += 'L'
            else:
                if hand == 'right':
                    answer += 'R'
                else:
                    answer += 'L'
        if answer[-1] == 'R':
            right = location[num]
        else:
            left = location[num]

    return answer