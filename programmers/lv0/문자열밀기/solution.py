def solution(A, B):
    if A == B : return 0

    s = A

    
    for i in range(len(A)-1):
        s = s[-1] + s[:-1]
        if s == B : return i+1

    return -1
    
