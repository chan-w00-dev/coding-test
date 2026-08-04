import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = []

    # 소수 제거
    for x in range(4,n+1):
        if is_prime(x):
            continue
        else :
            answer.append(x)

    return len(answer)
