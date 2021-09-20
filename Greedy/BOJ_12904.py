# BOJ 12904
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/12904

import sys

input = sys.stdin.readline

S = list(input())
S = S[:-1]
T = list(input())
T = T[:-1]

def reverse_operator_1(lst):
    lst = lst[:-1]
    return lst
    
def reverse_operator_2(lst):
    lst = lst[:-1]
    return lst[::-1]
    

while len(T) != len(S):
    if T[-1] == "A":
        T = reverse_operator_1(T)
    elif T[-1] == "B":
        T = reverse_operator_2(T)
        
if T == S:
    print(1)
    
else:
    print(0)
