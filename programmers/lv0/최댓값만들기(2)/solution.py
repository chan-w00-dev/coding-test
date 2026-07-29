from itertools import combinations
    
def solution(numbers):
    max = -10000000000
    for x in combinations(numbers, 2):
        if (x[0] * x[1]) > max:
            max = x[0] * x[1]
    return max