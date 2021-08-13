# BOJ 10162
# Author: Gu Lee
# Date: 2021.07.14
# Source: https://www.acmicpc.net/problem/10162

n = int(input())

times = [300, 60, 10]
result = []

if n%10:
  print(-1)

else:
  for time in times:
    result.append(n//time) 
    n %= time

  print(result[0], result[1], result[2], end=" ")