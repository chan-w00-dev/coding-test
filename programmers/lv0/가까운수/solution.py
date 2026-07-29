def solution(array, n):
    dif = 1000
    answer = 1000
    for x in array:
        if (x - n) ** 2 < dif ** 2:
            answer = x
            dif =  x - n
        elif (x - n) ** 2 == dif ** 2:
            if answer > x:
                answer = x
                dif = x - n
    return answer