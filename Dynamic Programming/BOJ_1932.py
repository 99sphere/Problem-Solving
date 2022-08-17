# BOJ 1932
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * (i+1) for i in range(n)]
arr = []

for i in range(n):
  arr.append(list(map(int, input().split())))

dp[0] = arr[0]

for i in range(1,n):
  for j in range(len(arr[i])):
    if j == 0:
      dp[i][j] = dp[i-1][j] + arr[i][j]
    elif j == len(arr[i]) - 1:
      dp[i][j] = dp[i-1][j-1] + arr[i][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

print(max(dp[-1]))
