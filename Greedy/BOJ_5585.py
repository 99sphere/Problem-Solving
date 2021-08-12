# BOJ 5585
# Author: Gu Lee
# Date: 2021.07.13
# Source: https://www.acmicpc.net/problem/5585

n = int(input())
change = 1000 - n
coins = [500, 100, 50, 10, 5, 1]
result = 0
for coin in coins:
  result += int(change/coin)
  change %= coin
print(result)