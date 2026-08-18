from itertools import combinations

def solution(numbers):
    answer = [sum(c) for c in combinations(numbers,2)]
    return sorted(list(dict.fromkeys(answer)))
