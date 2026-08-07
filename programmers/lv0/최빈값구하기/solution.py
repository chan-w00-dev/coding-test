from collections import Counter

def solution(array):
    array_counts = Counter(array)
    
    if len(array) == 1:
        return array[0]
    
    top_two = array_counts.most_common(2)

    if top_two[0][1] == top_two[1][1]:
        return -1
    else :
        return top_two[0][0]