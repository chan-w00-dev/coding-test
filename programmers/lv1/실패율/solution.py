from collections import Counter

def solution(N, stages):
    cnt = Counter(stages)

    s = cnt[N+1]
    reach =[0] * N
    for i in range(N,0,-1):
        s+=cnt[i]
        reach[i-1] = s

    fail = [cnt[i] for i in range(1,N+1)]
    
    fail_ratio = [f/r if r != 0 else 0 for f,r in zip(fail,reach)]
    
    answer = sorted(range(1,N+1), key = lambda x: (-fail_ratio[x-1],x))
    return answer

