from collections import Counter
def solution(participant, completion):
    cntParticipant = Counter(participant)
    cntCompletion = Counter(completion)

    rest = cntParticipant - cntCompletion
    answer = list(rest.elements())[0]
    
    return answer