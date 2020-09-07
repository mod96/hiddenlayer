def solution(d, budget):
    d.sort()
    for idx, price in enumerate(d):
        budget -= price
        if budget < 0:
            return idx
    return len(d)