def solution(s):
    l = s.split()

    numbers = [n if n == "Z" else int(n) for n in l]
    answer = 0

    # for i in range(len(numbers)):
    #     if(numbers[i] == "Z"):
    #         answer -= numbers[i-1]
    #     else : answer += numbers[i]

    for i, x in enumerate(numbers):
        if x == "Z":
            answer -= numbers[i-1]
        else : answer += x
        
    return answer


