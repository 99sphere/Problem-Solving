# BOJ 16120
# Author: Gu Lee
# Date: 2021.09.21
# Source: https://www.acmicpc.net/problem/16120

string = input()

if string == "P" or string == "PPAP":
    print("PPAP")
    
else:
    stack = []
    ppap = ['P', 'P', 'A', 'P']
    for i in string:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()
    if stack == ppap or stack == ['P']:
        print('PPAP')
    else:
        print('NP')
