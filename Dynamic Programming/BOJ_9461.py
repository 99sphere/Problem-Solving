# BOJ 9461
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
dp[6] = 4
dp[7] = 5
dp[8] = 7
dp[9] = 9
dp[10] = dp[5]+dp[9]
dp[11] = dp[6]+dp[10]
for i in range(10, 100):
  dp[i] = dp[i-1] + dp[i-5]

for i in range(t):
  n = int(input())
  print(dp[n-1])
