# BOJ 1010
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/1010

import sys
from itertools import combinations


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                dp[i][j] = j
                continue
                
            if i == j:
                dp[i][j] = 1
            
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    print(dp[n][m])
