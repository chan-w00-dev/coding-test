n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_coins = 0

# 3x3 격자의 왼쪽 위 모서리 (r, c) 좌표를 기준으로 탐색
for r in range(n - 2):
    for c in range(n - 2):
        # (r, c)부터 (r+2, c+2)까지 3x3 범위의 동전 개수 합산
        current_coins = sum(
            grid[i][j]
            for i in range(r, r + 3)
            for j in range(c, c + 3)
        )
        max_coins = max(max_coins, current_coins)

print(max_coins)