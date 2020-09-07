phone_book=['119', '97674223', '1195524421']

def solution(phone_book):
    phone_book.sort()
    TF=True
    for i in range(len(phone_book)-1):
        if len(phone_book[i])<len(phone_book[i+1]):
            front=phone_book[i]
            targ=phone_book[i+1]
            for j in range(len(front)):
                if front[j]!=targ[j]:
                    TF=True
                    break
                else:
                    TF=False
            if TF==False:
                return TF

    return TF