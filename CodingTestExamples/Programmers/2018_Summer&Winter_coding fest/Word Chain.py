def solution(n, words):
    bag = []
    for idx, word in enumerate(words):
        if word in bag or (idx > 0 and word[0] != words[idx-1][-1]):
            return [idx % n + 1, idx // n + 1]
        else:
            bag.append(word)

    return [0,0]
