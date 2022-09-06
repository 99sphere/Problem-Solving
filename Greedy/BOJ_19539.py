# BOJ 19539
# Author: Gu Lee
# Date: 2022.09.06
# Source: https://www.acmicpc.net/problem/19539

from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
sum = 0

remain = defaultdict(int)

for num in nums:
    remain[2] += num // 2
    remain[1] += num % 2

if ((remain[2]-remain[1])) % 3 == 0 and remain[2] >= remain[1]:
    print("YES")

else:
    print("NO")
