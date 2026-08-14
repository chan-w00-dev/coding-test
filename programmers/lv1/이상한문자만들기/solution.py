def solution(s):
    arr = s.split(" ")
    answer = []
    for word in arr:
        for i, char in enumerate(word):
            if i%2 == 0:
                answer.append(char.upper())
            else:
                answer.append(char.lower())
        answer.append(" ")
        
    return "".join(answer[:-1])


