# BOJ 11659
# Author: Gu Lee
# Date: 2022.01.30
# Source: https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(n):
  dp[i+1] = dp[i] + nums[i]

for i in range(m):
  i, j = map(int, input().split())
  print(dp[j]-dp[i-1])
