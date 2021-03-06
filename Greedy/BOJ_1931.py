# BOJ 1931
# Author: Gu Lee
# Date: 2021.07.31
# Source: https://www.acmicpc.net/problem/1931

n = int(input())
meetings = []
for i in range(n):
  start, end = map(int, input().split())
  meetings.append((start, end))

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
time = 0
cnt = 0
for start, end in meetings:
  if start >= time:
    time = end
    cnt += 1
print(cnt)