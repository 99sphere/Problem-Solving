# BOJ 1439
# Author: Gu Lee
# Date: 2022.08.18
# Source: https://www.acmicpc.net/problem/1439

import sys
from collections import deque

input = sys.stdin.readline

arr = list(input().rstrip())

zero_to_one = 0
one_to_zero = 0

if arr[0] == "1":
    zero_to_one += 1
else:
    one_to_zero += 1

for i in range(len(arr)-1):
    if arr[i] == "1" and arr[i+1] == "0":
        one_to_zero += 1

    elif arr[i] == "0" and arr[i+1] == "1":
        zero_to_one += 1

print(min(zero_to_one, one_to_zero))

