# BOJ 9095
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/9095

dp = [1, 2, 4]
for i in range(3, 10):
  dp.append(dp[i-1] + dp[i-2] + dp[i-3])

T = int(input())
for _ in range(T):
  n = int(input())
  print(dp[n-1])
