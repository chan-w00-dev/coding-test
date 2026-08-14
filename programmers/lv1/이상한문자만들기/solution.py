def solution(s):
    arr = s.split(" ")
    answer = []
    for word in arr:
        w = [char.upper() if i%2 == 0 else char.lower() for i, char in enumerate(word)]
        answer.append("".join(w))
        
    return " ".join(answer)



