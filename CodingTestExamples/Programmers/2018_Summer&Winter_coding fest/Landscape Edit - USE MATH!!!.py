'''def solution(land, P, Q):
    N = len(land)

    def return_price(h):
        price = 0
        for row in range(N):
            for col in range(N):
                targ = land[row][col]
                if targ > h:
                    price += (targ - h) * Q
                elif targ < h:
                    price += (h - targ) * P
        return price

    left = 0
    right = 10**9
    while True:
        mid = (left + right)//2
        mid_price0 = return_price(mid - 1)
        mid_price1 = return_price(mid)
        mid_price2 = return_price(mid + 1)
        if mid_price1 <= mid_price0 and mid_price1 <= mid_price2:
            return mid_price1
        elif mid_price0 <= mid_price1:
            right = mid - 1
        elif mid_price2 <= mid_price1:
            left = mid + 1
'''

'''def solution(land, P, Q):
    left = 0
    right = max([max(row) for row in land])
    while True:
        mid = (left + right)//2
        mid_price0, mid_price1, mid_price2 = 0, 0, 0
        for row in land:
            for targ in row:
                if targ > mid - 1:
                    mid_price0 += (targ - mid + 1) * Q
                elif targ < mid - 1:
                    mid_price0 += (mid - targ - 1) * P
                if targ > mid:
                    mid_price1 += (targ - mid) * Q
                elif targ < mid:
                    mid_price1 += (mid - targ) * P
                if targ > mid + 1:
                    mid_price2 += (targ - mid - 1) * Q
                elif targ < mid + 1:
                    mid_price2 += (mid - targ + 1) * P

        if mid_price1 <= mid_price0 and mid_price1 <= mid_price2:
            return mid_price1
        elif mid_price0 < mid_price1:
            right = mid - 1
        else:                           # mid_price2 < mid_price1
            left = mid + 1'''

'''def solution(land, P, Q):
    left = 0
    right = max([max(row) for row in land])
    saved_val = {}
    while True:
        mid = (left + right)//2
        mid_price0, mid_price1, mid_price2 = 0, 0, 0
        found0, found2 = mid-1 in saved_val, mid+1 in saved_val
        for row in land:
            for targ in row:
                if not found0:
                    if targ > mid - 1:
                        mid_price0 += (targ - mid + 1) * Q
                    elif targ < mid - 1:
                        mid_price0 += (mid - targ - 1) * P
                if targ > mid:
                    mid_price1 += (targ - mid) * Q
                elif targ < mid:
                    mid_price1 += (mid - targ) * P
                if not found2:
                    if targ > mid + 1:
                        mid_price2 += (targ - mid - 1) * Q
                    elif targ < mid + 1:
                        mid_price2 += (mid - targ + 1) * P
        if found0:
            mid_price0 = saved_val[mid-1]
        else:
            saved_val[mid-1] = mid_price0
        saved_val[mid] = mid_price1
        if found2:
            mid_price2 = saved_val[mid+1]
        else:
            saved_val[mid+1] = mid_price2
        if mid_price1 <= mid_price0 and mid_price1 <= mid_price2:
            return mid_price1
        elif mid_price0 < mid_price1:
            right = mid - 1
        else:                           # mid_price2 < mid_price1
            left = mid + 1'''

def return_price(land, P, Q, h):
    price = 0
    for row in land:
        for targ in row:
            if targ > h:
                price += (targ - h) * Q
            elif targ < h:
                price += (h - targ) * P
    return price

def solution(land, P, Q):
    sort_land = sorted([elt for row in land for elt in row])
    idx = int(Q * len(sort_land) / (P + Q))
    return return_price(land, P, Q, sort_land[idx])



print(solution([[1,2],[2,3]],3,2))
print(solution([[4,4,3],[3,2,2],[2,1,0]],5,3))
