# BOJ 12865
# Author: Gu Lee
# Date: 2022.09.10
# Source: https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())

items = [[0, 0]]
for _ in range(n):
    items.append(list(map(int, input().split())))
dp = [[0] * (k+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, k+1):
        w = items[i][0]
        v = items[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k]) 
