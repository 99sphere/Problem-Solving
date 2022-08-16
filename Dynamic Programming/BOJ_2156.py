# BOJ 2156
# Author: Gu Lee
# Date: 2022.08.16
# Source: https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline


n = int(input())

arr = [0] * 10000

for i in range(n):
  arr[i] = int(input().rstrip())
  
dp = [0] * 10000

dp[0] = arr[0]
dp[1] = dp[0] + arr[1]
dp[2] = max(dp[0] + arr[2], dp[1], arr[1]+arr[2]) 

for i in range(3, n):
  dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2]+arr[i], dp[i-1])

print(max(dp))
