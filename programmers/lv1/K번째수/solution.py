def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1

        new_array = sorted(array[i:j])
        answer.append(new_array[k])

    return answer
