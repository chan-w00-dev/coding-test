def solution(score):
    s = [sum(x) for x in score]

    answer = [sum(x > n for x in s) + 1 for n in s]

    return answer
