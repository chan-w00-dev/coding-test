from collections import Counter

def solution(array):
    array_counts = Counter(array)
    max_val = max(array_counts.values())
    max_keys = [n for n, count in array_counts.items() if count == max_val]

    if len(max_keys) > 1:
        return -1
    else :
        return max_keys[0]
