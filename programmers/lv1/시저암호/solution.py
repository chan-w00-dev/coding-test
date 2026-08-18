def shift (char, n):
    push = ord(char) + n
    if (push > 90 and ord(char) < 91) or (push > 122 and 96 < ord(char)):
        push -= 26
    elif char == " ":
        push -= n
    return chr(push)

def solution(s, n):
    answer = [shift(char, n) for char in s]

    return "".join(answer)

