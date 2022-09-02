# BOJ 2812
# Author: Gu Lee
# Date: 2022.09.02
# Source: https://www.acmicpc.net/problem/2812

n, k = map(int, input().split())

nums = list(list(input()))
stack = []

for i, num in enumerate(nums):
    if not stack:
        stack.append(num)
        continue 

    while len(stack) > 0 and k > 0 and int(stack[-1]) < int(num):
        k -= 1
        stack.pop()

    stack.append(num)

answer = "".join(stack)

if k > 0:
    answer = answer[:-k]

print(answer)
