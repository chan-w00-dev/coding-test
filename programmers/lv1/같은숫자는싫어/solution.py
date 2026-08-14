def solution(arr):
    l = [(arr[0]+1)] + arr[:]
    answer = [a for a,b in zip(arr,l) if a != b]
    return answer