# BOJ 1789
# Author: Gu Lee
# Date: 2021.09.19
# Source: https://www.acmicpc.net/problem/1789

s = int(input())
count = 0
i = 1
while True:
  next = s - i
  if next > i:
    count += 1
    i += 1
    s = next
  else:
    break

print(count+1)
