# BOJ 11053
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/11053

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 1001

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j] and dp[i] < dp[j]:
      dp[i] = dp[j]
  dp[i] += 1

print(max(dp))
