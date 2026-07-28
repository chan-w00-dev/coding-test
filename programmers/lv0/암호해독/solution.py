def solution(cipher, code):
    arr = list(cipher)
    index = code - 1
    answer = ""
    for i in range(len(arr)//code):
        answer += arr[index]
        index += code
    return answer