# BOJ 1912
# Author: Gu Lee
# Date: 2022.08.16
# Source: https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]

for i in range(n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
print(max(dp))
