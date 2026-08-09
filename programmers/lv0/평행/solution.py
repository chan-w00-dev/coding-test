import itertools
def solution(dots):
    combo = itertools.combinations(dots, 2)
    tan = [(dot[0][1] - dot[1][1]) / (dot[0][0] - dot[1][0]) for dot in combo]
    if len(set(tan)) != len(tan):
        return 1
    else:
        return 0