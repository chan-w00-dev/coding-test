import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = [x for x in range(4,n+1) if not is_prime(x)]

    return len(answer)
