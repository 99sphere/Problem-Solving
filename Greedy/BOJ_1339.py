# BOJ 1339
# Author: Gu Lee
# Date: 2021.09.22
# Source: https://www.acmicpc.net/problem/1339
import sys
input = sys.stdin.readline

n = int(input())
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0,
'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
answer = 0
words = [input().strip('\n') for _ in range(n)]

for alphabet in words:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet)-1 - i)
        alphabet_dict[alphabet[i]] += num

for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)
