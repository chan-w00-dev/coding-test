def solution(spell, dic):
    s = set(spell)

    return int(any(d for d in dic if s == set(d))) or 2


        
