def solution(lottos, win_nums):
    zeroCount = lottos.count(0)

    correct = set(lottos) & set(win_nums)

    minRank = min(6, 7 - len(correct))

    maxRank = max(1, minRank - zeroCount)

    return [maxRank,minRank]
    