def solution(score):
    answer = [0 for i in range(len(score))]
    s = [sum(x) for x in score]

    for i, n in enumerate(s):
        rank = 1
        for x in s:
            if x > n:
                rank += 1
        answer[i] = rank

    return answer
