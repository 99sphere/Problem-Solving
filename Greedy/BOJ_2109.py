# BOJ 2109
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/2109

import sys

input = sys.stdin.readline

n = int(input())
pay_and_due = [list(map(int, input().split())) for _ in range(n)]
pay_and_due = sorted(pay_and_due, key = lambda x: (-x[0], x[1]))

schd = [0 for _ in range(10001)]

for i in range(n):
    for j in range(pay_and_due[i][1], 0, -1):
        if pay_and_due[i][0] > schd[j]:
            schd[j] = pay_and_due[i][0]
            break

print(sum(schd))
