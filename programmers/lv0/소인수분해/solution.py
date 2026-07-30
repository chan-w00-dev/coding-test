def solution(n):
    divisior = []

    #Even
    if n % 2 == 0:
        divisior.append(2)

    #Odd 약수이면서 prime
    for i in range(3, n+1, 2):
        if n % i == 0:
            divisior.append(i)

            for j in range(3, int(i**0.5)+1, 2):
                if i % j == 0:
                    divisior.remove(i)
                    break

    #자기 자신과 1을 제외한 약수가 존재하지 않을 때
    if len(divisior) == 0 : divisior.append(n)

    return divisior

    
    
