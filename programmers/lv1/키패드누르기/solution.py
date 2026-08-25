# numbers	hand	result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

def solution(numbers, hand):
    keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    pos = {val:(r,c) for r, row in enumerate(keypad) for c, val in enumerate(row)}

    L = -1
    R = -2
    answer = ""
#1. 왼손 오른손 어디에 있는지
    for n in numbers:
        if n in (1,4,7):
            L = n
        elif n in (3,6,9):
            R = n

#2. 2,5,8,0 차례 왼손 오른손 거리확인(로직 필요)
        else :
            index_N = pos[n]
            index_R = pos[R]
            index_L = pos[L]

            distance_L = abs(index_N[0]-index_L[0])+abs(index_N[1]-index_L[1])
            distance_R = abs(index_N[0]-index_R[0])+abs(index_N[1]-index_R[1])

            # if distance_L > distance_R:
            #     R = n
            # elif distance_R > distance_L:
            #     L = n
            # else:
            #     if hand == "right":
            #         R = n
            #     else : 
            #         L = n

            chosen_hand = min([["l",distance_L],["r",distance_R]], key = lambda x: (x[1], x[0] != hand[0]))

            if chosen_hand[0].upper() == "L": L = n
            else : R = n

        if n == R:
            answer += "R"
        elif n == L:
            answer += "L"

    return answer

