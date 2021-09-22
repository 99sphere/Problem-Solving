# BOJ 2141
# Author: Gu Lee
# Date: 2021.09.22
# Source: https://www.acmicpc.net/problem/2141

import sys
input = sys.stdin.readline

n = int(input())

total_people = 0
dist_and_people = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    total_people += dist_and_people[i][1]

dist_and_people = sorted(dist_and_people)


# 과반수를 넘어야 하기 때문에, 전체 인구수가 홀수인 경우 mid + 1
if total_people%2 == 0:
    mid = total_people//2
else:
    mid = total_people//2 + 1

cnt = 0
for i in range(n):
    cnt += dist_and_people[i][1]
    if cnt >= mid:
        print(dist_and_people[i][0])
        break
