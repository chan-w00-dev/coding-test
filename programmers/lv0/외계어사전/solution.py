def solution(spell, dic):
    s = "".join(sorted(spell))

    for x in dic:
        d = "".join(dict.fromkeys(sorted(x)))

        if s == d:
            return 1

    return 2
        
