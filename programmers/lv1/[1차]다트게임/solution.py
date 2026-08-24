def solution(dartResult):   
    num = [str(x) for x in range(0,11)]
    bonus_dict = {
        "S" : 1,
        "D" : 2,
        "T" : 3
    }
    option = ["*","#"]
    idx = 0
    score = [0] * 3


    for i, x in enumerate(dartResult):
        
        if x == "1" and dartResult[i+1] == "0":
            score[idx] = 10
        elif x == "0" and dartResult[i-1] == "1":
            continue
        elif x in num:
            score[idx] = int(x)

        if x in bonus_dict:
            score[idx] = score[idx] ** bonus_dict.get(x)
            idx += 1

        if x in option:
            if x == "*" and idx >= 2:
                score[idx-2] *= 2
                score[idx-1] *= 2
                
            elif x == "*" and idx == 1:
                score[idx-1] *= 2

            elif x == "#":
                score[idx-1] *= -1

    return sum(score)

            


    