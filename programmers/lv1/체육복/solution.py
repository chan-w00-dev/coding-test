def solution(n, lost, reserve):
    t=set(lost) & set(reserve)

    lost = set([x for x in lost if x not in t])
    reserve = set([x for x in reserve if x not in t])

    hasCloth = [False if i+1 in lost else True for i in range(n)]

    for i, cloth in enumerate(hasCloth):
        if not cloth:
            if i in reserve:
                hasCloth[i] = True
                reserve.discard(i)
            elif i+2 in reserve:
                hasCloth[i] = True
                reserve.discard(i+2)

    return sum(hasCloth)

