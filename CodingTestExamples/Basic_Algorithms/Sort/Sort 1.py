def solution(array, commands):
    l=len(commands)
    answer=[0]*l
    for i in range(l):
        answer[i]=sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1]
    return answer