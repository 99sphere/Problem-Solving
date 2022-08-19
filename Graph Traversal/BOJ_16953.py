# BOJ 16953
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/16953

import sys
from collections import deque

input = sys.stdin.readline

if __name__ =="__main__":
    a, b = map(int, input().split())
    answer = False
    queue = deque()
    queue.append((a, 1))
    while queue:
        start, cnt = queue.popleft()
        new_val = [start*2, int(str(start)+"1")]
        for val in new_val:
            if val <= b:
                if val == b:
                    answer = True
                    print(cnt+1)
                    answer = True
                    break
                else:
                    queue.append((val, cnt+1))
                    continue
    if not answer:
        print(-1)
