from collections import Counter

def solution(s):
    d = Counter(s)
    answer = []

    for x in d:
        if d[x] == 1:
            answer.append(x)

    return "".join(sorted(answer))
            

