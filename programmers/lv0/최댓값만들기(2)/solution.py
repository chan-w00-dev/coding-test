# from itertools import combinations
    
def solution(numbers):
    # return max(x[0]*x[1] for x in combinations(numbers,2))
    numbers = sorted(numbers)
    return max(numbers[0]*numbers[1], numbers[-2]*numbers[-1])
    
