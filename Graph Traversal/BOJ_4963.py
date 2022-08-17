# BOJ 4963
# Author: Gu Lee
# Date: 2022.08.17
# Source: https://www.acmicpc.net/problem/4963

import sys
from collections import deque

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))

    queue = deque()
    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                queue.append((i, j))
                answer += 1
                while queue:
                    start_i, start_j = queue.popleft()
                    arr[i][j] = 0
                    dx = [1, -1, 0, 0, 1, 1, -1, -1]
                    dy = [0, 0, 1, -1, 1, -1, 1, -1]

                    for k in range(8):
                        nx = start_j + dx[k]
                        ny = start_i + dy[k]
                        if 0 <= nx < w and 0 <= ny < h and arr[ny][nx] == 1:
                            arr[ny][nx] = 0
                            queue.append((ny, nx)) 
    print(answer)
