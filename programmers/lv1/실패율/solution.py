from collections import Counter

def solution(N, stages):
    cnt = Counter(stages)
    reach = [sum(cnt[i] for i in range(1,N+2) if i >= j) for j in range(1,N+1)]
    fail = [cnt[i] for i in range(1,N+1)]
    
    fail_ratio = [f/r if r != 0 else 0 for f,r in zip(fail,reach)]
    
    answer = sorted(range(1,N+1), key = lambda x: (-fail_ratio[x-1],x))
    return answer

