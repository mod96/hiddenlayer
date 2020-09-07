'''def solution(numbers):
    temp={}
    for num in numbers:
        num_str=str(num)
        l=len(num_str)
        if l==3:
            temp.setdefault(num_str,[]).append(num_str)
        elif l==2:
            key=num_str+num_str[0]
            temp.setdefault(key,[]).append(num_str)
        elif l==1:
            if num_str=='0':
                temp.setdefault(num_str,[]).append(num_str)
            else:
                key=num_str*3
                temp.setdefault(key,[]).append(num_str)
        else:
            temp.setdefault('0', []).append(num_str)

    answer=''
    for key in reversed(sorted(temp)):
        if int(key[0])>=int(key[1]):
            for elt in reversed(sorted(temp[key])):
                answer+=elt
        else:
            for elt in sorted(temp[key]):
                answer+=elt

    return answer


from random import randint
numbers=[randint(0,1001) for _ in range(100)]
print(numbers)
print(solution(numbers))'''

def solution(numbers):
    def keyftn(num):
        l=len(str(num))
        if l==3:
            return num
        elif l==2:
            key=str(num)
            if key[0]<key[1]:
                return int(key+key[0])+0.5
            else:
                return int(key+key[0])-0.5
        elif l==1:
            key = str(num)
            return int(key*3)
        else:
            return 0.5

    numbers.sort(key=keyftn,reverse=True)
    answer=''

    for num in numbers:
        answer+=str(num)
    if answer[0]=='0':
        return '0'
    else:
        return answer

numbers=[0, 0, 0, 0, 0]
print(numbers)
print(solution(numbers))