import math
a = int(input())
b = int(input())
c = int(input())
P = a + b + c
p = P / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S)
