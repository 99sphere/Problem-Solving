# BOJ 11727
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/11727

n = int(input())

dp = [0] * n

if n == 1:
  print(1)
else:
  dp[0] = 1
  dp[1] = 3

  for i in range(2, n):
    dp[i] = dp[i-1] + 2 * dp[i-2]
  print(dp[n-1]%10007)
