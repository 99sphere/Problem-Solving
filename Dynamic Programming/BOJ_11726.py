# BOJ 11726
# Author: Gu Lee
# Date: 2022.08.15
# Source: https://www.acmicpc.net/problem/11726

dp = [1, 2, 3]

for i in range(4,1001):
  dp.append(dp[-1] + dp[-2])
n = int(input())
print(dp[n-1]%10007)
