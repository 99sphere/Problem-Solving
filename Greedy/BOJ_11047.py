# BOJ 11047
# Author: Gu Lee
# Date: 2021.07.23
# Source: https://www.acmicpc.net/problem/11047

n, val = map(int, input().split())
coins = []
for i in range(n):
  coins.append(int(input()))
coins.reverse()
result = 0
i = 0
while val:
  result += (val//coins[i])
  val %= coins[i] 
  i += 1

print(result)