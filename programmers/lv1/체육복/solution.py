def solution(n, lost, reserve):
    hasCloth = [True] * n
    t=list(set(lost) & set(reserve))

    for x in t:
        lost.remove(x)
        reserve.remove(x)

    for i in lost:
        hasCloth[i-1] = False

    for i, cloth in enumerate(hasCloth):
        if not cloth:
            if i in reserve:
                hasCloth[i] = True
                reserve.remove(i)
            elif i+2 in reserve:
                hasCloth[i] = True
                reserve.remove(i+2)

    return sum(hasCloth)

