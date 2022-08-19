# BOJ 9466
# Author: Gu Lee
# Date: 2022.08.19
# Source: https://www.acmicpc.net/problem/9466

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(i):
    global made
    
    visited[i] = True
    team.append(i)

    next = arr[i]

    if visited[next] == True:
        if next in team:
            made += team[team.index(next):]  # 1 -> 3, 3 -> 3 인 경우 3 혼자 팀. 그러니, team에서 다음 next가 처음 등장한 인덱스 이후로 추가된 애들끼리만 한 팀으로 만들어야 함
        return

    else:
        dfs(next)

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [0] + list(map(int, input().split()))
        visited = [False] * (n+1) 
        made = []

        for i in range(1, n+1):
            if visited[i] == False:
                team = []
                dfs(i)
        print(n - len(made))
