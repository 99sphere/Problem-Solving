# BOJ 1461
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/1461

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
book_locs = list(map(int, input().split()))

plus = []
minus = []
final = 0
answer = 0

for book_loc in book_locs:
    if book_loc > 0:
        plus.append(book_loc)
    else:
        minus.append(book_loc)

    if abs(book_loc) > abs(final):
        final = book_loc

plus.sort(reverse=True)
minus.sort()

result = []

for i in range(0, len(plus), m):
    if plus[i] != final:
        result.append(plus[i])

for i in range(0, len(minus), m):
    if minus[i] != final:
        result.append(minus[i])

answer = abs(final)
for i in result:
    answer += abs(i * 2)

print(answer)
