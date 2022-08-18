# BOJ 1904
# Author: Gu Lee
# Date: 2022.08.18
# Source: https://www.acmicpc.net/problem/1904

import sys
from collections import deque

input = sys.stdin.readline


if n == 1:
    print(1)
else:
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    print(dp[-1])
