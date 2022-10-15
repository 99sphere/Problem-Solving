# BOJ 1041
# Author: Gu Lee
# Date: 2022.10.15
# Source: https://www.acmicpc.net/problem/1041

n = int(input())
nums = list(map(int, input().split()))

def one_side():
    return min(nums)

def two_side():
    arr = [min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])]
    arr = sorted(arr)
    return sum(arr[:2])

def three_side():
    arr = [min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])]
    arr = sorted(arr)
    return sum(arr[:])

def five_side():
    return sum(nums) - max(nums)

if n > 2:
    answer = 4 * three_side() + (8 * n - 12) * two_side() + ((n-2)**2 + 4*(n-1)*(n-2)) * one_side()
elif n == 2:
    answer = 4 * three_side() + 4 * two_side()
else:
    answer = five_side()

print(answer)
