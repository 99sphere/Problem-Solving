# BOJ 2941
# Author: Gu Lee
# Date: 2021.07.06
# Source: https://www.acmicpc.net/problem/2941

croatia_alphabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]
string = input()
result = 0

while string != "":
  prev = result
  for x in croatia_alphabet:
    if string[:3] == x:
      result += 1
      string = string[3:]
      continue
    
    elif string[:2] == x:
      result += 1
      string = string[2:]
      continue

  if result == prev:
    string = string[1:]
    result += 1

print(result)