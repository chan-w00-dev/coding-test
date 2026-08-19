from itertools import cycle

def solution(answers):
    answer = []

    arr1 = cycle([1,2,3,4,5])
    arr2 = cycle([2,1,2,3,2,4,2,5])
    arr3 = cycle([3,3,1,1,2,2,4,4,5,5])

    num1 = [next(arr1) for _ in range(len(answers))]
    num2 = [next(arr2) for _ in range(len(answers))]
    num3 = [next(arr3) for _ in range(len(answers))]

    first = sum(1 for x,n in zip(num1,answers) if x == n)
    second = sum(1 for x,n in zip(num2,answers) if x == n) 
    third = sum(1 for x,n in zip(num3,answers) if x == n)

    max_correct = max(first, second, third)

    for i, n in enumerate([first,second,third],start=1):
        if n == max_correct:
            answer.append(i)

    return answer