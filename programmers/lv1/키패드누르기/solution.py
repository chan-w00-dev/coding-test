# numbers	hand	result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"

def solution(numbers, hand):
    keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
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
            # print(n,L,R)
            for r, row in enumerate(keypad):
                for c, val in enumerate(row):
                    if val == n:
                        indexN = (r,c)
                    if val == R:
                        indexR = (r,c)
                    if val == L:
                        indexL = (r,c)

            distanceL = abs(indexN[0]-indexL[0])+abs(indexN[1]-indexL[1])
            distanceR = abs(indexN[0]-indexR[0])+abs(indexN[1]-indexR[1])
            # print(indexN,indexL,indexR)
            # print(distanceL,distanceR)

            if distanceL > distanceR:
                R = n
            elif distanceR > distanceL:
                L = n
            else:
                if hand == "right":
                    R = n
                else : 
                    L = n

        if n == R:
            answer += "R"
        elif n == L:
            answer += "L"

    return answer

