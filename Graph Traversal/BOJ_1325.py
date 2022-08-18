# BOJ 1325
# Author: Gu Lee
# Date: 2022.08.18
# Source: https://www.acmicpc.net/problem/1325

import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

trust_dict = defaultdict(list)
answer = []

for i in range(m):
    a, b = map(int, input().split())
    trust_dict[b-1].append(a-1)


for i in range(n):
    visited = [False for _ in range(n)]
    queue = deque()
    cnt = 0
    queue.append(i)
    visited[i] = True   
    cnt += 1
    while queue:
        start = queue.popleft()
        for j in trust_dict[start]:
            if visited[j] == False:
                cnt += 1
                queue.append(j)
                visited[j] = True
                
    answer.append(cnt)

answer_idx = []
for i, val in enumerate(answer):
    if val == max(answer):
        print(i+1, end = " ")
