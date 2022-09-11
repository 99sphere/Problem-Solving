# BOJ 9251
# Author: Gu Lee
# Date: 2022.09.11
# Source: https://www.acmicpc.net/problem/9251

import sys

input = sys.stdin.readline

word_1 = input().rstrip()
word_2 = input().rstrip()

n = len(word_1)
m = len(word_2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word_1[i-1] == word_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[i][j])
