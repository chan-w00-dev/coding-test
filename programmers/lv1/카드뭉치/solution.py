def solution(cards1, cards2, goal):
    for g in goal:
        if cards1 and cards1[0] == g:
            cards1.remove(g)
        elif cards2 and cards2[0] == g:
            cards2.remove(g)
        else: 
            return "No"
    return "Yes"
