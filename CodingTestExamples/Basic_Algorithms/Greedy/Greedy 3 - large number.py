'''def solution(number, k):
    answer=''
    while k>0:
        M=max(number[0:k+1])
        idx=number.find(M)
        answer+=M
        number=number[idx+1:]
        k-=idx

    answer+=number

    return answer'''

def solution(number, k):
    answer=''
    idx=-1
    l=len(number)
    while k>0 and idx+1<l:
        try:
            for x in ['9', '8', '7', '6', '5', '4', '3', '2', '1','0']:
                if x in number[idx+1:idx+k+2]:
                    M=x
                    break
        except:
            for x in ['9', '8', '7', '6', '5', '4', '3', '2', '1','0']:
                if x in number[idx+1:]:
                    M=x
                    break
        idx_before=int(idx)
        idx=number.find(M,idx+1)
        answer+=M
        k-=(idx-idx_before-1)

    answer+=number[idx+1:]

    if k>0:
        return str(int(answer[:-k]))
    else:
        return str(int(answer))

print(solution('4177252841',4))
print(solution('9999',3))