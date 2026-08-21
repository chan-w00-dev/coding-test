from collections import Counter
def solution(participant, completion):
    cntParticipant = Counter(participant)
    cntCompletion = Counter(completion)

    rest = cntParticipant - cntCompletion
    answer = next(iter(rest))

    return answer