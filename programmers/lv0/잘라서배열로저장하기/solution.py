import math

def solution(my_str, n):
    temp = math.ceil(len(my_str) / n)
    answer = []

    for i in range(temp):
        start = i*n
        stop = (i+1)*n
        s = my_str[start:stop]
        answer.append(s)

    return answer
