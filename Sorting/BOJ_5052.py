# BOJ 5052
# Author: Gu Lee
# Date: 2022.09.16
# Source: https://www.acmicpc.net/problem/5052

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    answer = True
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    nums = sorted(nums)

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            answer = False

    if answer:
        print("YES")
    else:
        print("NO") 
