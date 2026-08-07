def solution(numlist, n):
    numlist.sort(key = lambda x : ((n-x)**2, -x))
    return numlist
