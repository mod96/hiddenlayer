def calc(num1,num2,op):
    if op == '*':
        return num1 * num2
    elif op == '+':
        return num1 + num2
    else:
        return num1 - num2

def solution(expression):
    ex_list = []
    temp = ''
    for elt in expression:
        if elt in {'*','+','-'}:
            ex_list.append(int(temp))
            ex_list.append(elt)
            temp = ''
        else:
            temp += elt
    ex_list.append(int(temp))

    possible = [['*','+','-'],['*','-','+'],['+','*','-'],['+','-','*'],['-','*','+'],['-','+','*']]
    answer = []
    for rec in possible:
        temp = list(ex_list)
        for elt in rec:
            while elt in temp:
                idx = temp.index(elt)
                temp[idx - 1] = calc(temp[idx - 1],temp[idx + 1],elt)
                del temp[idx]
                del temp[idx]
        answer.append(abs(temp[0]))

    return max(answer)

print(solution("100-200*300-500+20"))