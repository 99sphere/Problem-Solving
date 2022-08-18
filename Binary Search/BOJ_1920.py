# BOJ 1920
# Author: Gu Lee
# Date: 2022.08.18
# Source: https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline


def binary_search(start, end, arr, target):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:    
        return binary_search(mid+1, end, arr, target)

    else:
        return binary_search(start, mid-1, arr, target)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    m = int(input())
    targets = list(map(int, input().split()))
    arr = sorted(arr)

    for target in targets:
        if binary_search(0, n-1, arr, target) == None:
            print(0)
        else:
            print(1)
