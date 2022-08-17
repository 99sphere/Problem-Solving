# BOJ 10844
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/10844

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]*10 for i in range(n)]
for i in range(len(dp[0])):
  dp[0][i] = 1
dp[0][0] = 0

for i in range(1,len(dp)):
  for j in range(len(dp[i])):
    if j == 0:
      dp[i][j] = dp[i-1][j+1]
    elif j == 9:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1])%1000000000)
