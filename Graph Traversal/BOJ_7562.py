# BOJ 7562
# Author: Gu Lee
# Date: 2022.11.15
# Source: https://www.acmicpc.net/problem/7562

from collections import deque


def bfs():
    size = int(input())
    cy, cx = map(int, input().split()) 
    ty, tx = map(int, input().split())

    visited = [[False] * size for _ in range(size)]
    visited[cy][cx] = True

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    queue = deque()
    queue.append([cy, cx, 0])
    while queue:
        y, x, dist = queue.popleft()

        if x == tx and y == ty:
            print(dist)
            return None

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if 0 <= nx < size and 0 <= ny < size and visited[ny][nx] == False:
                visited[ny][nx] = True
                queue.append([ny, nx, dist+1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        bfs()
