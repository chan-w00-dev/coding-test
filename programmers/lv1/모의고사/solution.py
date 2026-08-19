def solution(answers):
    answer = []

    num1 = [i for i in range(1,6)] * (len(answers)//5)
    if len(answers) % 5 != 0:
        num1 += [i for i in range(1,len(answers) % 5 + 1)]

    arr2 = [1,3,4,5] * (len(answers)//8 + 1)
    num2 = [arr2[x//2-1] if x%2 == 0 else 2 for x in range(1,len(answers)+1)]

    arr3 = [3,3,1,1,2,2,4,4,5,5]
    num3 = arr3 * (len(answers)//10)
    if len(answers) % 10 != 0:
        num3 += arr3[:len(answers)%10]

    first = 0
    second = 0 
    third = 0

    for f,s,t,n in zip(num1,num2,num3,answers):
        if f == n:
            first += 1
        if s == n:
            second += 1
        if t == n:
            third += 1

    max_correct = max(first, second, third)

    if first == max_correct:
        answer.append(1)
    if second == max_correct:
        answer.append(2)
    if third == max_correct:
        answer.append(3)

    return answer